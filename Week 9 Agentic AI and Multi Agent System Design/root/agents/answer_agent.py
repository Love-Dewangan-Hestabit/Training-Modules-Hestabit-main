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
- Based on the question and the summary provide the final answer shouldn't be judgemental but comparision based. 
""",

        model_client=model_client,
        model_context=BufferedChatCompletionContext(buffer_size=10)
    )

    return answer_agent