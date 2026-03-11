from autogen_agentchat.agents import AssistantAgent


def create_research_agent(model_client):

    research_agent = AssistantAgent(
        name="research_agent",

        system_message="""
You are a Research Agent.

Your job:
- Collect factual information about the topic.

Rules:
- Do NOT summarize
- Do NOT answer the question
- Only provide raw research information
""",

        model_client=model_client,
    )

    return research_agent