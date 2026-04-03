from autogen_agentchat.agents import AssistantAgent
from autogen_core.model_context import BufferedChatCompletionContext

def create_research_agent(model_client):

    research_agent = AssistantAgent(
        name="research_agent",

        system_message="""
You are a Research Agent.

Your job:
- Collect factual information about the topic.

Rules:
- Do NOT summarize the information
- Do NOT answer the question
- Only provide raw research information
""",

        model_client=model_client,
        model_context=BufferedChatCompletionContext(buffer_size=2)
    )

    return research_agent