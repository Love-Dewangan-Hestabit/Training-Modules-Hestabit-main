import sqlite3
import csv
from autogen_core.tools import FunctionTool


async def show_db_tables(db_path: str) -> str:
    """Show all tables and their columns in a SQLite database. Input: db_path"""
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = cursor.fetchall()

        if not tables:
            conn.close()
            return "No tables found."

        result = ""
        for (table,) in tables:
            cursor.execute(f"PRAGMA table_info({table})")
            columns = cursor.fetchall()
            col_list = ", ".join(col[1] for col in columns)
            result += f"Table: {table}\nColumns: {col_list}\n\n"

        conn.close()
        return result

    except Exception as e:
        return f"Error: {e}"


async def query_database(db_path: str, query: str) -> str:
    """Run a SQL query on a SQLite database file. Input: db_path and query"""
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute(query)

        if query.strip().upper().startswith("SELECT"):
            rows = cursor.fetchall()
            col_names = [col[0] for col in cursor.description]
            result = " | ".join(col_names) + "\n"
            result += "-" * 40 + "\n"
            for row in rows:
                result += " | ".join(str(x) for x in row) + "\n"
            conn.close()
            return f"{len(rows)} rows found:\n{result}"
        else:
            conn.commit()
            conn.close()
            return "Query executed successfully."

    except Exception as e:
        return f"Database error: {e}"


async def import_csv_to_db(csv_path: str, db_path: str, table_name: str) -> str:
    """Import a CSV file into a SQLite database. Input: csv_path, db_path, table_name"""
    try:
        with open(csv_path, newline="") as f:
            reader = csv.DictReader(f)
            rows = list(reader)

        if not rows:
            return "Error: CSV file is empty."

        columns = list(rows[0].keys())
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        col_defs = ", ".join(f'"{col}" TEXT' for col in columns)
        cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
        cursor.execute(f"CREATE TABLE {table_name} ({col_defs})")

        placeholders = ", ".join("?" for _ in columns)
        for row in rows:
            values = [row[col] for col in columns]
            cursor.execute(f"INSERT INTO {table_name} VALUES ({placeholders})", values)

        conn.commit()
        conn.close()
        return f"Imported {len(rows)} rows into table '{table_name}'. Columns: {', '.join(columns)}"

    except Exception as e:
        return f"Error: {e}"



show_db_tables = FunctionTool(
    show_db_tables,
    description="Show all tables and columns in a SQLite database. Input: db_path"
)

query_database = FunctionTool(
    query_database,
    description="Run a SQL query on a SQLite database. Input: db_path and query"
)

import_csv_to_db = FunctionTool(
    import_csv_to_db,
    description="Import a CSV file into a SQLite database. Input: csv_path, db_path, table_name"
)