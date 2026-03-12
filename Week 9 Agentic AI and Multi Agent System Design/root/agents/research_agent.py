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
- Dont make the research information more than 600 words
""",

        model_client=model_client,
        model_context=BufferedChatCompletionContext(buffer_size=10)
    )

    return research_agent