from autogen_agentchat.agents import AssistantAgent
from autogen_core.model_context import BufferedChatCompletionContext


def create_validator_agent(model_client):

    validator = AssistantAgent(
        name="validator_agent",

        system_message="""
        You are a Validator Agent.
        
        Your job:
        Check the answer and fix issues if needed.
        
        Strict Rules:
        - Make sure answer is logical and factually correct
        - Do not increase length
        - Keep it concise
        - Only fix errors if present
        - Return final clean answer
        """,

        model_client=model_client
    )

    return validator