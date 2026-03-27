from autogen_agentchat.agents import AssistantAgent

def create_critic_agent(model_client):

    return AssistantAgent(
        name="critic_agent",
        model_client=model_client,

        system_message="""
You are a Critic Agent.

Your job:
- Identify flaws
- Find missing information
- Detect incorrect logic

Output:
- Issues
- Improvements
"""
    )