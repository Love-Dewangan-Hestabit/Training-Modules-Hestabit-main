from autogen_agentchat.agents import AssistantAgent

def create_analyst_agent(model_client):

    return AssistantAgent(
        name="analyst_agent",
        model_client=model_client,

        system_message="""
You are a Data Analyst Agent.

Your job:
- Analyze structured/unstructured data
- Extract insights
- Suggest business decisions

Rules:
- Be precise
- Use structured format
"""
    )