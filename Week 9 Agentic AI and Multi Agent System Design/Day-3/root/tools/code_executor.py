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
            - ALWAYS use provided context
            - DO NOT re-read CSV if DB output is present
            - ALL files are inside "data/" folder
            - ALWAYS read files like: data/filename.csv
            - ALWAYS save files inside "data/output/" folder
            - Handle case-insensitive matching
            - Print final output
            - NO markdown
            - NO explanations
            """
        )

    async def execute(self, context: str):
        response = await self.agent.run(task=context)
        code = response.messages[-1].content

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