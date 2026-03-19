from autogen_agentchat.agents import AssistantAgent
from autogen_core.model_context import BufferedChatCompletionContext


def create_worker_agent(model_client):

    worker = AssistantAgent(
        name="worker_agent",

        system_message="""
        You are a Worker Agent.
        
        Your job:
        Answer ONLY the given task.
        
        STRICT RULES:
        - Be concise (max 3-5 lines)
        - NO repetition
        - NO re-explaining previous tasks
        - NO introduction or conclusion
        - Use bullet points if helpful
        """,

        model_client=model_client,
        model_context=BufferedChatCompletionContext(buffer_size=5)
    )

    return worker