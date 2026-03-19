import json
import re
import os
from autogen_agentchat.agents import AssistantAgent

BASE_PATH = "data"


class FileAgent:
    def __init__(self, model_client):
        self.agent = AssistantAgent(
            name="file_agent",
            model_client=model_client,
            system_message="""
You are a File Agent.

STRICT RULES:
- You ONLY perform file operations
- DO NOT generate content on your own
- DO NOT explain anything
- If content is not provided → return error

Return ONLY JSON:
{
  "action": "read OR write",
  "file_name": "file.txt",
  "content": "ONLY if write"
}
"""
        )

    async def execute(self, task: str):
        response = await self.agent.run(task=task)
        raw = response.messages[-1].content

        print("\n[FILE AGENT RAW]\n", raw)

        cleaned = re.sub(r"```json|```", "", raw).strip()

        try:
            data = json.loads(cleaned)

            action = data["action"]
            file_name = data["file_name"]

            file_path = os.path.join(BASE_PATH, file_name)

            os.makedirs(BASE_PATH, exist_ok=True)

            if action == "write":
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(data.get("content", ""))
                return f"✅ File written: {file_path}"

            elif action == "read":
                if not os.path.exists(file_path):
                    return f"❌ File not found: {file_path}"

                with open(file_path, "r", encoding="utf-8") as f:
                    return f.read()

        except Exception as e:
            return f"File Agent Error: {str(e)}"