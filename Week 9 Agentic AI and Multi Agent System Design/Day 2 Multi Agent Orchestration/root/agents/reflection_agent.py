from autogen_agentchat.agents import AssistantAgent
from autogen_core.model_context import BufferedChatCompletionContext


def create_reflection_agent(model_client):

    reflection = AssistantAgent(
        name="reflection_agent",

        system_message="""
        You are a Reflection Agent.
        
        Your job:
        Review and improve the answer without changing its structure.
        
        Strict Rules:
        - Do not change the meaning of the answer
        - Do not remove important content
        - Remove repetition
        - Merge similar points
        - Keep answer short and structured
        - Max 150-200 words
        - Use headings and bullet points
        """,

        model_client=model_client
    )

    return reflection