import sqlite3
import sqlparse
from tabulate import tabulate

from utils.schema_loader import SchemaLoader
from generator.sql_generator import SQLGenerator


class SQLPipeline:
    def __init__(self, db_path):
        self.db_path = db_path
        self.schema_loader = SchemaLoader(db_path)
        self.generator = SQLGenerator()

    # --------------------------------------------------
    # VALIDATE SQL
    # --------------------------------------------------
    def validate_sql(self, sql):
        parsed = sqlparse.parse(sql)
        if not parsed:
            raise ValueError("Invalid SQL")

        statement = parsed[0]

        if statement.get_type() != "SELECT":
            raise ValueError("Only SELECT queries are allowed")

        if ";" in sql[:-1]:
            raise ValueError("Multiple statements are not allowed")

        forbidden = ["DROP", "DELETE", "UPDATE", "INSERT", "ALTER"]
        for word in forbidden:
            if word.lower() in sql.lower():
                raise ValueError("Dangerous SQL detected")

        return True

    # --------------------------------------------------
    # EXECUTE SQL
    # --------------------------------------------------
    def execute_sql(self, sql):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        try:
            cursor.execute(sql)
            rows = cursor.fetchall()
            columns = [desc[0] for desc in cursor.description]
            conn.close()
            return columns, rows
        except Exception as e:
            conn.close()
            raise e

    # --------------------------------------------------
    # RUN PIPELINE (OPTIMIZED)
    # --------------------------------------------------
    def run(self, question):

        schema = self.schema_loader.load_schema()

        # 1️⃣ Generate SQL (1 API call)
        sql = self.generator.generate_sql(question, schema)
        print("\nGenerated SQL:\n", sql)

        self.validate_sql(sql)

        # 2️⃣ Try execution
        try:
            columns, rows = self.execute_sql(sql)

        except Exception as e:
            print("SQL failed. Attempting correction...")
            
            # 2️⃣ Correction attempt (1 API call only if needed)
            sql = self.generator.correct_sql(sql, str(e), schema)
            print("\nCorrected SQL:\n", sql)

            self.validate_sql(sql)
            columns, rows = self.execute_sql(sql)

        if not rows:
            return {
                "sql": sql,
                "result": "No results found."
            }

        # ❌ Removed LLM summarization (saves API call)

        result_table = tabulate(rows, headers=columns, tablefmt="grid")

        return {
            "sql": sql,
            "result": result_table
        }