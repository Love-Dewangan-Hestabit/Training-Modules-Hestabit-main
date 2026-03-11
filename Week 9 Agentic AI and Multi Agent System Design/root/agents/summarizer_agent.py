from autogen_agentchat.agents import AssistantAgent


def create_summarizer_agent(model_client):

    summarizer_agent = AssistantAgent(
        name="summarizer_agent",

        system_message="""
You are a Summarizer Agent.

Your job:
- Convert research information into a concise summary.

Rules:
- Do NOT add new information
- Do NOT answer the question
- Only summarize the research
""",

        model_client=model_client,
    )

    return summarizer_agent