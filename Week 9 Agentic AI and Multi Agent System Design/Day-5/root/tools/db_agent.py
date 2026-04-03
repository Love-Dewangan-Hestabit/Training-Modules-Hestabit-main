import sqlite3
import re
import os
import pandas as pd
from autogen_agentchat.agents import AssistantAgent

class DBAgent:
    def __init__(self, model_client):
        self.agent = AssistantAgent(
            name="db_agent",
            model_client=model_client,
            system_message="""
You are a SQL Generation Agent for NEXUS AI.

Given a natural language query, column names, and sample data, return a single SQLite-compatible SQL query for a table named "data".

STRICT RULES:
1. Return ONLY the raw SQL statement.
2. No markdown fences (e.g., no ```sql), no explanation, no comments.
3. Use SQLite syntax (e.g., LENGTH() instead of LEN(), use CAST(x AS REAL)).
4. Table name is always: data.
5. Use the provided column names exactly (case-sensitive).
6. If the user query is vague ("analyze", "give insights"), perform a general summary (e.g., SELECT * FROM data LIMIT 10).
7. For row counts, use COUNT(*).
"""
        )

    SEARCH_DIRS = [
        "",           
        "data",
        "data/input",
        "data/output",
        "nexus_ai/data",
        "input",
        "uploads",
    ]

    def _resolve_csv(self, csv_path: str) -> str | None:
        """Return the first existing path for csv_path, searching SEARCH_DIRS."""
        candidates = []
        candidates.append(csv_path)
        filename = os.path.basename(csv_path)
        for d in self.SEARCH_DIRS:
            candidates.append(os.path.join(d, filename) if d else filename)
        
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        for d in self.SEARCH_DIRS:
            candidates.append(os.path.join(project_root, d, filename))

        for c in candidates:
            if os.path.isfile(c):
                return c
        return None

    async def execute(self, query: str, csv_path: str) -> str:

        resolved = self._resolve_csv(csv_path)
        if resolved is None:
            return f"[DB ERROR] File '{csv_path}' not found in searchable directories."
        csv_path = resolved

        try:
            df_full = pd.read_csv(csv_path)
            columns = ", ".join(df_full.columns.tolist())
            sample_data = df_full.head(3).to_string(index=False)
            schema_context = f"Columns: {columns}\nSample Data:\n{sample_data}"
        except Exception as e:
            return f"[DB ERROR] Could not read CSV schema: {e}"

        response = await self.agent.run(
            task=f"Schema Context:\n{schema_context}\n\nUser Task: {query}"
        )
        
        sql_raw = response.messages[-1].content if response.messages else ""
        
        sql_query = re.sub(r"```(?:sql)?\s*|```", "", sql_raw).strip()
        sql_query = sql_query.replace("\n", " ")

        sql_query = sql_query.split(';')[0].strip() + ";"

        print(f"\n[DB AGENT] Resolved CSV → {csv_path}")
        print(f"[DB AGENT] SQL Generated → {sql_query}")

        try:
            conn = sqlite3.connect(":memory:")
            df_full.to_sql("data", conn, index=False, if_exists="replace")
            
            result_df = pd.read_sql_query(sql_query, conn)
            conn.close()
            
            if result_df.empty:
                return "The query returned no results."
            
            return result_df.to_string(index=False)

        except Exception as e:
            return f"[DB ERROR] SQL Execution Failed: {e}\nQuery attempted: {sql_query}"