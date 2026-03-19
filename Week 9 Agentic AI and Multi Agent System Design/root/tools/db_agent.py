import sqlite3
import pandas as pd
from autogen_agentchat.agents import AssistantAgent


class DBAgent:
    def __init__(self, model_client):
        self.agent = AssistantAgent(
            name="db_agent",
            model_client=model_client,
            system_message="""
Convert user query to SQL.

STRICT RULES:
- Return ONLY SQL
- No explanation
- No markdown
- SQLite compatible
- Table name = data
"""
        )

    async def execute(self, task: str, csv_path: str):
        response = await self.agent.run(task=task)
        sql_query = response.messages[-1].content.strip()

        print("\n[SQL GENERATED]\n", sql_query)

        try:
            conn = sqlite3.connect(":memory:")
            df = pd.read_csv(csv_path)
            df.to_sql("data", conn, index=False, if_exists="replace")

            result = pd.read_sql_query(sql_query, conn)
            return result.to_string()

        except Exception as e:
            return f"DB Error: {str(e)}"