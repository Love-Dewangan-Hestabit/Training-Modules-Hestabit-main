import asyncio
import json
import re

from config import get_model_client
from tools.code_executor import CodeExecutorAgent
from tools.file_agent import FileAgent
from tools.db_agent import DBAgent
from autogen_agentchat.agents import AssistantAgent


class Orchestrator:
    def __init__(self):
        self.model_client = get_model_client()

        # ✅ STRICT PLANNER
        self.planner = AssistantAgent(
            name="planner",
            model_client=self.model_client,
            system_message="""
You are a planner.

Return ONLY JSON:
{
  "tools": ["file", "code", "db"]
}

STRICT RULES:
- No extra fields
- No explanation
- Only "tools"
"""
        )

        self.file_agent = FileAgent(self.model_client)
        self.db_agent = DBAgent(self.model_client)
        self.code_agent = CodeExecutorAgent(self.model_client)

    async def run(self, query: str):

        print("\n[USER QUERY]:", query)

        # 🔹 STEP 1: PLAN
        plan_response = await self.planner.run(task=query)
        raw_output = plan_response.messages[-1].content

        print("\n[PLANNER RAW OUTPUT]\n", raw_output)

        try:
            plan = json.loads(re.sub(r"```json|```", "", raw_output).strip())
            tools = plan.get("tools", ["code"])
        except:
            tools = ["code"]

        # ✅ FORCE FILE TOOL
        if any(word in query.lower() for word in [".txt", ".csv", "file", "write", "create", "save"]):
            if "file" not in tools:
                tools.insert(0, "file")

        print("\n[TOOLS SELECTED]:", tools)

        context = ""

        # Only use FileAgent for explicit read/write requests
        if "file" in tools and ("read" in query.lower()):
            file_res = await self.file_agent.execute(query)
            context += f"\n=== FILE OUTPUT ===\n{file_res}\n"

        # 🔹 STEP 3: DB
        if "db" in tools:
            db_res = await self.db_agent.execute(query, "data/sales.csv")
            context += f"\n=== DB OUTPUT ===\n{db_res}\n"

        # 🔹 STEP 4: CODE (MAIN LOGIC + WRITE FILE)
        if "code" in tools:
            code_res = await self.code_agent.execute(
                f"""
User Query:
{query}

Context:
{context}

Instructions:
- Use DB OUTPUT if available
- DO NOT create fake data
- Save result file inside data/
"""
            )
            context += f"\n=== CODE OUTPUT ===\n{code_res}\n"

        # 🔹 STEP 5: FINAL
        final_agent = AssistantAgent(
            name="final_agent",
            model_client=self.model_client,
            system_message="""
Only summarize given outputs.
Do NOT hallucinate.
"""
        )

        final = await final_agent.run(
            task=f"""
User Query:
{query}

Tool Outputs:
{context}

Provide final answer.
"""
        )

        return final.messages[-1].content


# RUN
if __name__ == "__main__":

    async def main():
        orch = Orchestrator()

        print("\n🚀 Multi-Agent System Started\n")

        while True:
            query = input("🧠 Enter your query: ")

            if query.lower() in ["exit", "quit"]:
                break

            try:
                result = await orch.run(query)

                print("\n========== FINAL ANSWER ==========\n")
                print(result)
                print("\n" + "="*50 + "\n")

            except Exception as e:
                print(f"\n❌ Error: {str(e)}\n")

    asyncio.run(main())