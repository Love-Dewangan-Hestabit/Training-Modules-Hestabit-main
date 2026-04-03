from autogen_agentchat.agents import AssistantAgent


def get_planner_agent(model):
    return AssistantAgent(
        name="PlanningAgent",
        description="Plans and delegates tasks. Always responds first.",
        model_client=model,
        system_message="""
        You are the planner. NEVER write code yourself.

        Your team:
        - CodeAgent : writes python code as plain text
        - FileAgent : reads files, writes text/reports to files
        - DBAgent   : runs SQL queries on databases

        For "generate/write code" tasks:
          → CodeAgent only. Just ask for the code. The system handles saving.

        For "read file" or "write a report/summary" tasks:
          → FileAgent only

        For "database or CSV query" tasks:
          → DBAgent only

        Rules:
        - NEVER ask FileAgent to save code — the system does that automatically
        - NEVER write code yourself
        - After CodeAgent writes the code, say TERMINATE
        - Keep it simple — one agent per task unless truly needed
        """
    )