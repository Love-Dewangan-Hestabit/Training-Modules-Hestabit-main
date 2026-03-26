from autogen_agentchat.agents import AssistantAgent
from autogen_core.model_context import BufferedChatCompletionContext


def create_worker_agent(model_client):

    worker = AssistantAgent(
        name="worker_agent",

        system_message="""
        You are a Worker Agent.
        
        Your job:
        Answer only the given task.
        
        Strict Rules:
        - Be concise (max 3-5 lines)
        - No re-explaining previous tasks
        - No introduction or conclusion
        - Use bullet points if helpful
        """,

        model_client=model_client
    )

    return worker