import json
import re
import os
import sys
import logging
import contextlib
import io
from datetime import datetime
from typing import Any

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from agents.planner_agent import create_planner_agent
from agents.tool_selector_agent import create_tool_selector_agent
from agents.research_agent import create_research_agent
from agents.analyst_agent import create_analyst_agent
from agents.critic_agent import create_critic_agent
from agents.optimizer_agent import create_optimizer_agent
from agents.validator import create_validator_agent
from agents.reporter_agent import create_reporter_agent
from tools.code_executor import CodeExecutorAgent
from tools.db_agent import DBAgent
from tools.file_agent import FileAgent
from config import get_model_client
from memory import (SessionMemory, LongTermMemory, VectorStore, MemorySummarizer)

os.makedirs("logs", exist_ok=True)

_file_handler = logging.FileHandler("logs/nexus.log")
_file_handler.setLevel(logging.DEBUG)
_file_handler.setFormatter(logging.Formatter("%(asctime)s  %(levelname)-7s  %(message)s"))

logging.root.setLevel(logging.DEBUG)
logging.root.handlers = [_file_handler]

for _lib in ("httpx", "httpcore", "openai", "autogen", "autogen_core",
             "autogen_agentchat", "autogen_ext"):
    logging.getLogger(_lib).setLevel(logging.WARNING)

log = logging.getLogger("nexus")



DIVIDER = "─" * 56

def _section(title: str) -> str:
    return f"\n{DIVIDER}\n  {title}\n{DIVIDER}"

def _step_banner(idx: int, agent: str, task: str) -> None:
    label = f"STEP {idx}  ▸  {agent.upper().replace('_', ' ')}"
    short_task = task if len(task) <= 90 else task[:87] + "..."
    print(f"\n{'─'*60}")
    print(f"  {label}")
    print(f"  ↳ {short_task}")
    print(f"{'─'*60}")

def _print_agent_output(agent_name: str, output: str) -> None:
    label = agent_name.replace("_", " ").title()
    print(f"\n  ┌─ {label} Output {'─' * (45 - len(label))}")
    for line in output.split("\n"):
        print(f"  │  {line}")
    print(f"  └{'─' * 50}")


def _extract_json(text: str) -> dict:

    cleaned = re.sub(r"```(?:json)?\s*|```", "", text).strip()

    match = re.search(r"\{.*\}", cleaned, re.DOTALL)
    if match:
        cleaned = match.group()
    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        try:
        
            import ast
            return ast.literal_eval(cleaned)
        except Exception:
            raise json.JSONDecodeError("Failed to extract valid JSON", text, 0)


def _is_read_task(task: str) -> bool:
    """
    Detect whether a file_agent invocation is a READ (needs to happen before
    the pipeline so agents have real data) vs a WRITE (must happen after the
    pipeline so the reporter output is available).

    Heuristic: if the user task contains read/open/load/show/analyse keywords
    aimed at a file AND no write/save/create/output keywords, treat as READ.
    """
    task_lower = task.lower()
    read_keywords  = {"read", "open", "load", "show", "display", "view",
                      "get", "fetch", "retrieve", "give", "insight", "analyze",
                      "analyse", "summarize", "summarise"}
    write_keywords = {"write", "save", "create", "output", "store", "export",
                      "generate", "produce", "make"}

    has_read  = any(kw in task_lower for kw in read_keywords)
    has_write = any(kw in task_lower for kw in write_keywords)


    return has_read and not has_write


class NexusOrchestrator:

    AGENT_FACTORIES = {
        "research_agent":  create_research_agent,
        "analyst_agent":   create_analyst_agent,
        "critic_agent":    create_critic_agent,
        "optimizer_agent": create_optimizer_agent,
        "validator_agent": create_validator_agent,
        "reporter_agent":  create_reporter_agent,
    }

    def __init__(self):
        api_key = os.getenv("GROQ_API_KEY") or os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise EnvironmentError(
                "No API key found. Set GROQ_API_KEY or OPENAI_API_KEY in your .env file."
            )

        self.model_client  = get_model_client()
        self.planner       = create_planner_agent(self.model_client)
        self.tool_selector = create_tool_selector_agent(self.model_client)
        self.code_executor = CodeExecutorAgent(self.model_client)
        self.db_agent      = DBAgent(self.model_client)
        self.file_agent    = FileAgent(self.model_client)

        self.session_memory = SessionMemory(max_messages=20)
        self.long_term      = LongTermMemory(db_path="memory/long_term.db")
        self.vector_store   = VectorStore(
            index_path="memory/faiss.index",
            meta_path="memory/meta.pkl",
        )
        self.summarizer     = MemorySummarizer(self.model_client)

        log.info("NexusOrchestrator initialised with memory system ✓")
        log.info("  Vector entries: %d | Long-term entries: %d",
                 self.vector_store.count(), self.long_term.count())

    async def run(self, user_task: str, ui_callback=None, active_files=None) -> str:
        log.info("NEW TASK: %s", user_task)
        log.info("ACTIVE FILES: %s", active_files)
        start = datetime.now()

        if ui_callback: ui_callback("phase", "MEMORY RECALL")
        print(_section("[MEMORY RECALL]"))
        memory_block = self._recall_memory(user_task)

        if ui_callback: ui_callback("phase", "TOOL SELECTION")
        print(_section("[TOOL SELECTION]"))
        tool_decision = await self._tool_selection(user_task)

        if ui_callback: ui_callback("phase", "PLANNING")
        print(_section("[PLANNING]"))
        plan = await self._plan(user_task, tool_decision)

        if ui_callback: ui_callback("phase", "EXECUTION")
        print(_section("[EXECUTION]"))
        final_output = await self._execute_plan(
            plan, user_task, tool_decision, memory_block, ui_callback, active_files
        )

        tools_used = ", ".join(tool_decision.get("tools") or [])
        await self._store_memory(user_task, final_output, tools_used)

        elapsed = (datetime.now() - start).total_seconds()
        log.info("TASK COMPLETE in %.1fs", elapsed)
        print(f"\n[DONE] Completed in {elapsed:.1f}s")

        return final_output

    def _recall_memory(self, user_task: str) -> str:
        parts = []

        similar = self.vector_store.search(user_task, k=3)
        if similar:
            print(f"  [SEARCH] Found {len(similar)} similar past interaction(s):")
            for i, mem in enumerate(similar, 1):
                summary = mem.get("summary", str(mem))
                print(f"      {i}. {summary[:100]}")
                parts.append(summary)
        else:
            print("  [INFO] No similar memories found.")

        recent = self.long_term.fetch_recent(limit=3)
        if recent:
            print(f"  [STORE] {len(recent)} recent long-term memor(y/ies) available.")
            for row in recent:
                parts.append(f"[Recent] {row[1]}") 

        session_fmt = self.session_memory.get_formatted()
        if self.session_memory.size() > 0:
            print(f"  [SESSION] Session buffer: {self.session_memory.size()} message(s).")

        if not parts and self.session_memory.size() == 0:
            return ""

        block = "=== MEMORY CONTEXT ===\n"
        if parts:
            block += "Relevant past interactions:\n"
            block += "\n".join(f"- {p}" for p in parts) + "\n\n"
        if self.session_memory.size() > 0:
            block += f"Session history:\n{session_fmt}\n"
        block += "=== END MEMORY ===\n"

        log.info("Memory block: %d chars", len(block))
        return block

    async def _store_memory(self, user_task: str, response: str, tools: str) -> None:
        self.session_memory.add("user", user_task)
        self.session_memory.add("assistant", response[:500])

        result = await self.summarizer.summarize(user_task, response)
        summary    = result["summary"]
        importance = result["importance"]

        if tools:
            importance = min(importance, 4)

        stored = self.long_term.store(
            user_task=user_task,
            agent_response=response,
            summary=summary,
            tools_used=tools,
            importance_score=importance,
        )

        if stored:

            self.vector_store.add(summary, {
                "summary": summary,
                "tools": tools,
                "timestamp": datetime.now().isoformat(),
            })
            log.info("Memory stored: importance=%d", importance)
        else:
            log.info("Memory skipped: importance=%d", importance)

    async def _tool_selection(self, task: str) -> dict:
        with contextlib.redirect_stdout(io.StringIO()):
            response = await self.tool_selector.run(task=task)
        raw = response.messages[-1].content.strip()
        log.debug("Tool selector raw: %s", raw)

        try:
            decision = _extract_json(raw)
        except (json.JSONDecodeError, AttributeError):
            decision = {"use_tool": False, "tools": [], "reason": "parse error"}

        if "tool" in decision and "tools" not in decision:
            t = decision.get("tool")
            decision["tools"] = [t] if t else []

        use    = decision.get("use_tool", False)
        tools  = decision.get("tools") or []
        reason = decision.get("reason", "")

        print(f"  {'[NEEDED] Tools needed: ' + ', '.join(tools) if use and tools else '[NONE] No tool required'}")
        print(f"  Reason: {reason}")
        log.info("Tool decision → use=%s  tools=%s", use, tools)
        return decision

    async def _plan(self, task: str, tool_decision: dict) -> list[dict]:
        augmented_task = task
        if tool_decision.get("use_tool"):
            tools = tool_decision.get("tools") or []
            augmented_task += (
                f"\n\n[TOOL CONTEXT] The following tools will be used for this task: "
                f"{', '.join(tools)}. Do NOT include them as pipeline steps."
            )

        with contextlib.redirect_stdout(io.StringIO()):
            response = await self.planner.run(task=augmented_task)
        raw = response.messages[-1].content.strip()
        log.debug("Planner raw: %s", raw)

        try:
            plan_json = _extract_json(raw)
            steps     = plan_json.get("steps", [])
        except (json.JSONDecodeError, AttributeError, KeyError) as exc:
            raise ValueError(f"Planner returned invalid JSON.\n{raw}") from exc

        if not steps:
            raise ValueError("Planner returned an empty step list.")

        print(f"\n  [PLAN] Execution plan — {len(steps)} step(s):\n")
        for i, step in enumerate(steps, 1):
            agent     = step.get("agent", "?")
            task_desc = step.get("task", "")
            short     = task_desc if len(task_desc) <= 100 else task_desc[:97] + "..."
            print(f"  {i}. [{agent}]  {short}")

        log.info("Plan: %s", [s["agent"] for s in steps])
        return steps

    async def _execute_plan(
        self,
        steps: list[dict],
        user_task: str,
        tool_decision: dict,
        memory_block: str = "",
        ui_callback=None,
        active_files=None,
    ) -> str:
        context_parts: list[str] = []
        if memory_block:
            context_parts.append(memory_block)
        context_parts.append(f"USER TASK:\n{user_task}")
        last_output = ""

        ALL_TOOL_NAMES = {"db_agent", "code_executor", "file_agent"}

        selected_tools = (tool_decision.get("tools") or []) if tool_decision.get("use_tool") else []

        file_agent_selected = "file_agent" in selected_tools
        file_is_read  = file_agent_selected and _is_read_task(user_task)
        file_is_write = file_agent_selected and not file_is_read

        pre_tools = [t for t in selected_tools if t in {"db_agent", "code_executor"}]
        if file_is_read:
            pre_tools.append("file_agent")

        post_tools = ["file_agent"] if file_is_write else []

        for tool_name in pre_tools:
            print(f"\n  [TOOL] Running tool: {tool_name.upper()}")
            log.info("Running pre-pipeline tool: %s", tool_name)
            tool_result = await self._run_tool(tool_name, user_task, active_files)
            context_parts.append(f"TOOL OUTPUT ({tool_name}):\n{tool_result}")
            print(f"  [SUCCESS] Tool output captured ({len(tool_result)} chars)")
            
            if ui_callback:
                ui_callback("tool", {"name": tool_name.upper(), "output": tool_result})

            if tool_name == "code_executor":
                print(f"  [RAW SCRIPT OUTPUT]:\n  {tool_result.replace(chr(10), chr(10) + '  ')}\n  {'-'*50}")
                
            log.info("Tool output length: %d", len(tool_result))

        for idx, step in enumerate(steps, 1):
            agent_name       = step.get("agent", "")
            task_instruction = step.get("task", "")

            _step_banner(idx, agent_name, task_instruction)
            log.info("Running step %d/%d: %s", idx, len(steps), agent_name)

            if agent_name in ALL_TOOL_NAMES:
                print(f"  [INFO] [{agent_name}] is a tool — handled separately. Skipping.")
                continue

            agent = self._get_agent(agent_name)
            if agent is None:
                print(f"  [WARN] Unknown agent '{agent_name}' — skipping.")
                continue

            full_prompt = self._build_prompt(task_instruction, context_parts)

            try:
                with contextlib.redirect_stdout(io.StringIO()):
                    response = await agent.run(task=full_prompt)
                output = response.messages[-1].content.strip()
            except Exception as exc:
                output = f"[ERROR in {agent_name}: {exc}]"
                log.error("Agent %s failed: %s", agent_name, exc)

            last_output = output
            if ui_callback:
                ui_callback("agent", {"name": agent_name, "output": output})
            context_parts.append(f"{agent_name.upper()} OUTPUT:\n{output}")
            _print_agent_output(agent_name, output)
            log.info("%s output length: %d", agent_name, len(output))

        for tool_name in post_tools:
            print(f"\n  [TOOL] Running tool: {tool_name.upper()} (post-pipeline write)")
            log.info("Running post-pipeline writer tool: %s", tool_name)
            write_context = "\n\n".join(context_parts) + f"\n\nORIGINAL TASK:\n{user_task}"
            tool_result = await self._run_tool(tool_name, write_context, active_files)
            if ui_callback:
                ui_callback("tool", {"name": tool_name.upper(), "output": tool_result})
            print(f"  [SUCCESS] {tool_result}")
            log.info("Writer tool result: %s", tool_result)

        return last_output

    def _get_agent(self, name: str) -> Any | None:
        factory = self.AGENT_FACTORIES.get(name)
        return factory(self.model_client) if factory else None

    @staticmethod
    def _build_prompt(task_instruction: str, context_parts: list[str]) -> str:
        context_block = "\n\n".join(context_parts)
        return (
            f"=== CONTEXT FROM PREVIOUS STEPS ===\n"
            f"{context_block}\n\n"
            f"=== YOUR CURRENT TASK ===\n"
            f"{task_instruction}"
        )

    async def _run_tool(self, tool_name: str, task: str, active_files=None) -> str:
        if tool_name == "code_executor":
            result = await self.code_executor.execute(task)
            if result["status"] == "success":
                return result.get("output", "")
            return f"[CODE ERROR] {result.get('error', 'Unknown error')}"

        elif tool_name == "db_agent":

            all_csvs = re.findall(r'[\w./\\-]+\.csv', task, re.IGNORECASE)
            
            if all_csvs:
                csv_path = all_csvs[0]
                log.info("db_agent: using explicit CSV from task -> %s", csv_path)
            elif active_files:

                csv_path = active_files[0]
                log.info("db_agent: using active file from UI -> %s", csv_path)
            else:

                return (
                    "[DB ERROR] No CSV file found. "
                    "Please upload a file via the UI or mention its name in your task."
                )
            
            return await self.db_agent.execute(task, csv_path)

        elif tool_name == "file_agent":
            return await self.file_agent.execute(task)

        return f"[TOOL ERROR] Unknown tool: {tool_name}"