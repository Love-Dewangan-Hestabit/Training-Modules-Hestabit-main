from autogen_agentchat.agents import AssistantAgent
from autogen_core.model_context import BufferedChatCompletionContext

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
- Concise summary to the level that user can easily understand
- Use Bullet points if necessary
- Dont make the summary more than 300 words
""",

        model_client=model_client,
        model_context=BufferedChatCompletionContext(buffer_size=10)
    )

    return summarizer_agent