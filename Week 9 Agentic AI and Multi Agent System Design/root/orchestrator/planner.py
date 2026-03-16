from autogen_agentchat.agents import AssistantAgent
from autogen_core.model_context import BufferedChatCompletionContext


def create_planner_agent(model_client):

    planner = AssistantAgent(
        name="planner_agent",

        system_message="""
You are a Planner Agent.

Your job:
Break the user query into smaller tasks.

Return tasks as a numbered list.

Example:
1. Task one
2. Task two
3. Task three
""",

        model_client=model_client,
        model_context=BufferedChatCompletionContext(buffer_size=10)
    )

    return planner