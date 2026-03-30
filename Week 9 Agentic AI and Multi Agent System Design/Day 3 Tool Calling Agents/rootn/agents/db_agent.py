from autogen_agentchat.agents import AssistantAgent
from tools.db_agent import show_db_tables, query_database, import_csv_to_db


def get_db_agent(model):
    return AssistantAgent(
        name="DBAgent",
        description="Runs SQL queries on SQLite databases and imports CSV files",
        model_client=model,
        tools=[show_db_tables, query_database, import_csv_to_db],
        system_message="""
        You work with SQLite databases.

        Your tools:
        - show_db_tables   : shows all tables and columns. Input: db_path
        - query_database   : runs a SQL query. Input: db_path, query
        - import_csv_to_db : imports a CSV into a database. Input: csv_path, db_path, table_name

        Rules:
        - Always call show_db_tables first before writing any SQL
        - If working with a CSV, use import_csv_to_db first
        - Use CAST(column AS REAL) for numeric operations in SQL
        - Return results clearly with row counts
        """
    )