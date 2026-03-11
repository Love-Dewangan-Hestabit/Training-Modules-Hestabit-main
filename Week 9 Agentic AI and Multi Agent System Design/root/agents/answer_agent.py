from autogen_agentchat.agents import AssistantAgent


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
""",

        model_client=model_client,
    )

    return answer_agent