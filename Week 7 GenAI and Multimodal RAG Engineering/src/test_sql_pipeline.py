import os
import re
import pandas as pd
import sqlite3
from datetime import datetime

from src.pipelines.sql_pipeline import SQLPipeline


def create_sqlite_from_file(file_path):
    file_name = os.path.splitext(os.path.basename(file_path))[0]
    table_name = re.sub(r'\W+', '_', file_name)

    db_path = f"{table_name}.db"
    conn = sqlite3.connect(db_path)

    if file_path.endswith(".csv"):
        df = pd.read_csv(file_path)
        df.to_sql(table_name, conn, if_exists="replace", index=False)

    elif file_path.endswith(".xlsx"):
        df = pd.read_excel(file_path)
        df.to_sql(table_name, conn, if_exists="replace", index=False)

    else:
        raise ValueError("Only CSV and Excel files supported.")

    conn.close()


    print("DATABASE CREATED SUCCESSFULLY")

    print(f"Database Name : {db_path}")
    print(f"Table Name    : {table_name}")


    return db_path


def print_formatted_answer(question, answer):
    print("SQL QUESTION ANSWERING SYSTEM")

    print("\n Question:")
    print(f"   {question}")

    print("\nResult:")
    print(answer)


def main():
    file_path = input("Enter CSV/Excel file path: ").strip()

    if not os.path.exists(file_path):
        print("File not found.")
        return

    db_path = create_sqlite_from_file(file_path)
    pipeline = SQLPipeline(db_path)

    while True:
        question = input("Enter your question (or type 'exit'): ")

        if question.lower() == "exit":
            print("\nExiting SQL-QA System.\n")
            break

        try:
            answer = pipeline.run(question)
            print_formatted_answer(question, answer)

        except Exception as e:
            print("\nError:", e, "\n")


if __name__ == "__main__":
    main()