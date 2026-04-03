import subprocess
import tempfile
import re
import os
from autogen_agentchat.agents import AssistantAgent


class CodeExecutorAgent:

    UNSAFE_PATTERNS = [
        "while True",
        "os.system(",
        "os.remove(",
        "os.unlink(",
        "os.rmdir(",
        "os.removedirs(",
        "import remove",
        "import rmdir",
        "import unlink",
        "import rmtree",
        "shutil.",
        "os.popen(",
        "subprocess",
        "__import__",
        "getattr(",
        "eval(",
        "exec(",
        "open(",         
        "pathlib",
        "socket.",
        "requests.",
        "urllib.",
    ]

    def __init__(self, model_client):
        self.agent = AssistantAgent(
            name="code_agent",
            model_client=model_client,
            system_message="""
You are a Python Code Generation Agent.

STRICT RULES:
- Use ONLY Python standard library (no pip installs)
- NEVER generate fake/sample data unless explicitly given
- ALWAYS use the context/data provided to you
- Write files ONLY inside "data/output/"
- Return ONLY raw executable Python code
- NO markdown fences, NO explanations, NO comments
- ALWAYS print ONLY the final result (single print statement)
- Keep output concise and deterministic
"""
        )

    async def execute(self, context: str) -> dict:
       
        response = await self.agent.run(task=context)
        code = response.messages[-1].content.strip()

        code = re.sub(r"```python\s*|```\s*", "", code).strip()

        for pattern in self.UNSAFE_PATTERNS:
            if pattern in code:
                return {
                    "status": "error",
                    "error": f"Unsafe pattern detected: {pattern}",
                    "output": None,
                }

        os.makedirs("data/output", exist_ok=True)

        with tempfile.NamedTemporaryFile(
            delete=False, suffix=".py", mode="w", encoding="utf-8"
        ) as f:
            f.write(code)
            file_path = f.name

        try:
            result = subprocess.run(
                ["python", file_path],
                capture_output=True,
                text=True,
                timeout=15,
            )

            stdout = result.stdout.strip()
            stderr = result.stderr.strip()

            if result.returncode == 0:
                output_str = f"=== GENERATED PYTHON SCRIPT ===\n{code}\n\n=== SCRIPT OUTPUT ===\n{stdout[:2000]}"
                return {
                    "status": "success",
                    "output": output_str,
                }
            else:
                err_str = f"=== GENERATED PYTHON SCRIPT ===\n{code}\n\n=== SCRIPT ERROR ===\n{stderr[:1000]}"
                return {
                    "status": "error",
                    "output": None,
                    "error": err_str,
                }

        except subprocess.TimeoutExpired:
            return {"status": "error", "output": None, "error": "Execution timed out (15s)"}

        except Exception as e:
            return {"status": "error", "output": None, "error": str(e)}

        finally:
            try:
                os.unlink(file_path)
            except Exception:
                pass