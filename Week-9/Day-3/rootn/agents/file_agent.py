from autogen_agentchat.agents import AssistantAgent
from tools.file_agent import read_file_content, write_file, list_files


def get_file_agent(model):
    return AssistantAgent(
        name="FileAgent",
        description="Reads and writes files",
        model_client=model,
        tools=[read_file_content, write_file, list_files],
        system_message="""
        You read and write files.

        When saving code:
        - Extract the code exactly from the previous message
        - Remove the markdown code fences (the triple backtick lines)
        - Save only the raw code using write_file
        - Keep all indentation exactly as written

        Rules:
        - Never read a file right after writing it
        - Confirm filename after saving
        """
    )