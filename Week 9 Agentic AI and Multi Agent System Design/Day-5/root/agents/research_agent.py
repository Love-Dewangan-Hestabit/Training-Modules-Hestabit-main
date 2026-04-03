from autogen_agentchat.agents import AssistantAgent
from autogen_core.model_context import BufferedChatCompletionContext


def create_research_agent(model_client):
    return AssistantAgent(
        name="research_agent",
        model_client=model_client,
        model_context=BufferedChatCompletionContext(buffer_size=4),
        system_message="""
You are a Research Agent in NEXUS AI.

Your job:
- Gather accurate, factual information relevant to the task
- Cover key concepts, frameworks, industry knowledge, and best practices
- Structure findings clearly with headings and bullet points

STRICT RULES:
- Only provide verified, factual information — no opinions or guesses
- Be thorough but concise (max 500 words)
- Always directly address what was asked
- Do not repeat the question back
"""
    )