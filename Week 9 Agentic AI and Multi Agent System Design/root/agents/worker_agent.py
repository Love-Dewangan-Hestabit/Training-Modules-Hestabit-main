from autogen_agentchat.agents import AssistantAgent
from autogen_core.model_context import BufferedChatCompletionContext


def create_worker_agent(model_client):

    worker = AssistantAgent(
        name="worker_agent",

        system_message="""
You are a Worker Agent.

Your job:
Execute the task assigned by the planner.

Rules:
- Focus only on the given task
- Produce clear results
""",

        model_client=model_client,
        model_context=BufferedChatCompletionContext(buffer_size=10)
    )

    return worker