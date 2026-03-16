from autogen_agentchat.agents import AssistantAgent
from autogen_core.model_context import BufferedChatCompletionContext


def create_validator_agent(model_client):

    validator = AssistantAgent(
        name="validator_agent",

        system_message="""
You are a Validator Agent.

Your job:
Check the final response for errors.

Verify:
- correctness
- logical consistency
- completeness

If issues exist, fix them.
Return the corrected answer.
""",

        model_client=model_client,
        model_context=BufferedChatCompletionContext(buffer_size=10)
    )

    return validator