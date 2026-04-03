from autogen_agentchat.agents import AssistantAgent

def create_reporter_agent(model_client):

    return AssistantAgent(
        name="reporter_agent",
        model_client=model_client,

        system_message="""
You are a Reporter Agent.

Your job:
- Present final result cleanly
- Use headings + bullet points
- Make it user-friendly
"""
    )