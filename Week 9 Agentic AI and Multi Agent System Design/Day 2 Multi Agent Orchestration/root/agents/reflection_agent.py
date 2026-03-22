from autogen_agentchat.agents import AssistantAgent
from autogen_core.model_context import BufferedChatCompletionContext


def create_reflection_agent(model_client):

    reflection = AssistantAgent(
        name="reflection_agent",

        system_message="""
        You are a Reflection Agent.
        
        Your job:
        Combine all worker outputs into ONE concise answer.
        
        STRICT RULES:
        - Remove repetition
        - Merge similar points
        - Keep answer SHORT and structured
        - Max 150-200 words
        - Use headings + bullet points
        """,

        model_client=model_client,
        model_context=BufferedChatCompletionContext(buffer_size=5)
    )

    return reflection