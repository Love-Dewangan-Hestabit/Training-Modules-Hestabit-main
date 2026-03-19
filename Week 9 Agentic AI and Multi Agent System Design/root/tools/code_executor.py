import subprocess
import tempfile
import re
from autogen_agentchat.agents import AssistantAgent


class CodeExecutorAgent:
    def __init__(self, model_client):
        self.agent = AssistantAgent(
            name="code_agent",
            model_client=model_client,
            system_message="""
You are a Python execution agent.

STRICT RULES:
- Use ONLY standard Python libraries
- NEVER generate fake/sample data
- ALWAYS use DB OUTPUT if available
- DO NOT re-read CSV if DB output is present
- ALWAYS write files inside "data/" folder
- Handle case-insensitive matching (e.g., Electronics/electronic)
- Print final output
- NO markdown
- NO explanations
"""
        )

    async def execute(self, task: str):
        response = await self.agent.run(task=task)
        code = response.messages[-1].content

        # ✅ REMOVE MARKDOWN
        code = re.sub(r"```python|```", "", code).strip()

        print("\n[CODE GENERATED]\n", code)

        with tempfile.NamedTemporaryFile(delete=False, suffix=".py") as f:
            f.write(code.encode())
            file_path = f.name

        try:
            result = subprocess.run(
                ["python", file_path],
                capture_output=True,
                text=True,
                timeout=20
            )
            return result.stdout or result.stderr

        except Exception as e:
            return f"Code Execution Error: {str(e)}"