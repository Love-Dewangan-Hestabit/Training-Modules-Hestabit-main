from autogen_agentchat.agents import AssistantAgent

def create_optimizer_agent(model_client):

    return AssistantAgent(
        name="optimizer_agent",
        model_client=model_client,

        system_message="""
You are an Optimizer Agent.

Your job:
- Improve outputs
- Make answers more efficient
- Remove unnecessary content

Return improved version only.
"""
    )