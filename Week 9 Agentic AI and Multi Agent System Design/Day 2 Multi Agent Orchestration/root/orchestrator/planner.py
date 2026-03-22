from autogen_agentchat.agents import AssistantAgent
from autogen_core.model_context import BufferedChatCompletionContext


def create_planner_agent(model_client):

    planner = AssistantAgent(
        name="planner_agent",

        system_message="""
        You are a Planner Agent.
        
        Your job:
        Break the user query into SMALL, CLEAR, NON-OVERLAPPING tasks.

        Step 1: Determine if the query is SIMPLE or COMPLEX.

        - SIMPLE = can be answered directly (definition, short explanation)
        - COMPLEX = requires multiple concepts or steps
        
        Step 2:
        - If SIMPLE -> return ONLY 1-2 tasks
        - If COMPLEX -> return up to 5 tasks
        
        STRICT RULES:
        - If the query is ambiguous, include tasks for ALL possible interpretations.
        - Return ONLY numbered tasks
        - Each task must be ONE LINE
        - Not more than 5 tasks but it's OK to return less if the query is simple.
        """,

        model_client=model_client,
        model_context=BufferedChatCompletionContext(buffer_size=5)
    )

    return planner