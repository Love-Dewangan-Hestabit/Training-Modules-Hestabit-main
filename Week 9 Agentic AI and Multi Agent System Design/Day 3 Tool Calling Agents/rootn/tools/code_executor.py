import sys
import io
import os
import subprocess
from autogen_core.tools import FunctionTool


async def run_python(code: str) -> str:
    """Execute a short python expression and return output"""
    output_capture = io.StringIO()
    sys.stdout = output_capture
    try:
        exec(code, {})
        result = output_capture.getvalue()
        return result if result else "Done."
    except Exception as e:
        return f"Error: {e}"
    finally:
        sys.stdout = sys.__stdout__


async def execute_file(file_path: str) -> str:
    """Execute a saved python file by filename"""
    try:
        if not os.path.exists(file_path):
            return f"Error: '{file_path}' not found."
        result = subprocess.run(
            [sys.executable, file_path],
            capture_output=True, text=True, timeout=10
        )
        output = result.stdout.strip()
        errors = result.stderr.strip()
        if errors:
            return f"Error:\n{errors}"
        return output if output else "Ran but printed nothing."
    except subprocess.TimeoutExpired:
        return "Error: Took too long."
    except Exception as e:
        return f"Error: {e}"


run_python_tool = FunctionTool(
    run_python,
    description="Run a short simple python expression. Input: code"
)

execute_file_tool = FunctionTool(
    execute_file,
    description="Execute a saved python file. Input: file_path"
)