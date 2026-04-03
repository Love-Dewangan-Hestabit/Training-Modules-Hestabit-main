import csv
import io as _io
import json
import re
import os
from autogen_agentchat.agents import AssistantAgent

BASE_PATH = "data"

SEARCH_DIRS = ["", "data", "data/input", "data/output", "nexus_ai/data", "input"]


def _resolve_file(file_name: str) -> str | None:
    """Search common locations for an existing file. Returns path or None."""
    candidates = [file_name]
    base = os.path.basename(file_name)
    for d in SEARCH_DIRS:
        candidates.append(os.path.join(d, base) if d else base)
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    for d in SEARCH_DIRS:
        candidates.append(os.path.join(project_root, d, base))
    for c in candidates:
        if os.path.isfile(c):
            return c
    return None


def _tabular_to_csv(tabular: str) -> str:
    """Convert pandas-style space-aligned table to proper CSV."""
    lines = [l for l in tabular.strip().splitlines() if l.strip()]
    if not lines:
        return ""
    rows = [re.split(r"\s{2,}", line.strip()) for line in lines]
    buf = _io.StringIO()
    writer = csv.writer(buf)
    for row in rows:
        writer.writerow(row)
    return buf.getvalue()


def _extract_section(context: str, marker: str) -> str:
    """Extract everything after `marker` up to the next double-newline+CAPS block."""
    if marker not in context:
        return ""
    start = context.index(marker) + len(marker)
    tail = context[start:]
    stop = re.search(r"\n\n[A-Z][A-Z_ ]+(?:OUTPUT|TASK):", tail)
    end = stop.start() if stop else len(tail)
    return tail[:end].strip()


class FileAgent:

    def __init__(self, model_client):
        self.agent = AssistantAgent(
            name="file_agent",
            model_client=model_client,
            system_message="""
You are a File Operation Agent.

Given a context describing a file task, return a JSON object describing the operation.

STRICT RULES:
- Return ONLY raw JSON (no markdown, no explanation)
- Supported actions: "read" or "write"
- For "read": omit "content"
- For "write": set "content" to the exact text that must be saved

CONTENT SELECTION RULES for "write" (check in this order):
1. If "TOOL OUTPUT (db_agent):" exists in context AND the file is a .csv
   → copy ALL rows from that block verbatim, converting space-aligned columns to CSV
2. Otherwise look for "REPORTER_AGENT OUTPUT:" in the context
   → use that block exactly as the content (this is the final answer to persist)
3. NEVER use the ORIGINAL TASK or USER TASK as content — those are instructions, not data
4. NEVER invent or summarise content

JSON format:
{
  "action": "write",
  "file_name": "output.txt",
  "content": "exact content here..."
}
{
  "action": "read",
  "file_name": "input.txt"
}
"""
        )

    async def execute(self, context: str) -> str:
        response = await self.agent.run(task=context)
        raw     = response.messages[-1].content.strip()
        cleaned = re.sub(r"```json\s*|```\s*", "", raw).strip()

        print(f"\n[FILE AGENT] Raw → {cleaned[:200]}")

        try:
            data = json.loads(cleaned)
        except json.JSONDecodeError as e:
            return f"[FILE ERROR] Could not parse JSON: {e}\nRaw: {cleaned}"

        action    = data.get("action", "").lower()
        file_name = data.get("file_name", "")

        if not file_name:
            return "[FILE ERROR] No file_name provided."

        if action == "read":
            resolved = _resolve_file(file_name)
            if resolved is None:
                return (
                    f"[FILE ERROR] File '{file_name}' not found.\n"
                    f"Please place it in the 'data/' folder next to main.py."
                )
            with open(resolved, "r", encoding="utf-8") as f:
                content = f.read()
            print(f"  [FILE AGENT] Read {len(content)} chars from {resolved}")
            return content

        elif action == "write":
            file_content = data.get("content", "").strip()

            if len(file_content) < 50:
                if file_name.lower().endswith(".csv"):
                    raw_table = _extract_section(context, "TOOL OUTPUT (db_agent):")
                    if raw_table and not raw_table.startswith("[DB ERROR]"):
                        file_content = _tabular_to_csv(raw_table)
                        print(f"  [FILE AGENT] Safety-net: CSV from db_agent ({len(file_content)} chars)")
                    else:
                        return f"[FILE ERROR] No DB data to write. db_agent returned: {raw_table or 'nothing'}"
                else:
                    reporter_out = _extract_section(context, "REPORTER_AGENT OUTPUT:")
                    if reporter_out:
                        file_content = reporter_out
                        print(f"  [FILE AGENT] Safety-net: using reporter output ({len(file_content)} chars)")
                    else:
                        return "[FILE ERROR] No content to write — reporter output not found in context."

            os.makedirs(BASE_PATH, exist_ok=True)
            file_path = os.path.join(BASE_PATH, file_name)
            with open(file_path, "w", encoding="utf-8", newline="") as f:
                f.write(file_content)
            return f"[SUCCESS] File written: {file_path} ({len(file_content)} chars)"

        else:
            return f"[FILE ERROR] Unknown action: {action}"