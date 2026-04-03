from autogen_agentchat.agents import AssistantAgent
from tools.code_executor import run_python_tool, execute_file_tool


def get_code_agent(model):
    return AssistantAgent(
        name="CodeAgent",
        description="Writes python code as plain text and executes saved files",
        model_client=model,
        tools=[run_python_tool, execute_file_tool],
        system_message="""
        You write python code.

        When asked to write code:
        - Write it as plain text in your message inside triple backticks
        - Do NOT use any tool to save it — the system handles saving automatically

        When asked to run or execute a saved file:
        - Use execute_file tool with the filename

        When asked a simple one-liner calculation:
        - Use run_python tool

        Never use pandas or external libraries.
        Always include a working example with print() in your code.
        """
    )