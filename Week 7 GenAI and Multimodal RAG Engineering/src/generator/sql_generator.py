from src.generator.llm_client import LLMClient


class SQLGenerator:
    def __init__(self):
        self.llm = LLMClient()

    def generate_sql(self, question, schema):
        prompt = f"""
You are a SQL expert.

Database Schema:
{schema}

Rules:
- Use only tables and columns from schema
- Only generate SELECT queries
- Do not explain anything
- Do not use markdown
- Return only valid SQL

Question:
{question}
"""

        sql = self.llm.generate(prompt)
        sql = sql.replace("```sql", "").replace("```", "").strip()
        return sql

    def correct_sql(self, sql, error, schema):
        prompt = f"""
The following SQL failed:

{sql}

Error:
{error}

Database Schema:
{schema}

Fix the SQL.
Return only corrected SQL.
"""

        corrected_sql = self.llm.generate(prompt)
        corrected_sql = corrected_sql.replace("```sql", "").replace("```", "").strip()
        return corrected_sql

    def summarize(self, question, result_table):
        prompt = f"""
User Question:
{question}

SQL Result:
{result_table}

Summarize the result clearly in 2-3 sentences.
"""

        return self.llm.generate(prompt)