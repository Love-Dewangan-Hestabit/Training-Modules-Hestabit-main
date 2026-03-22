from autogen_agentchat.agents import AssistantAgent
from autogen_core.model_context import BufferedChatCompletionContext

def create_answer_agent(model_client):

    answer_agent = AssistantAgent(
        name="answer_agent",

        system_message="""
You are an Answer Agent.

Your job:
- Use the summary provided
- Produce the final answer.

Rules:
- Do NOT perform research
- Do NOT summarize again
- Only provide the final answer based on the Research and Summary provided
""",

        model_client=model_client,
        model_context=BufferedChatCompletionContext(buffer_size=2)
    )

    return answer_agent