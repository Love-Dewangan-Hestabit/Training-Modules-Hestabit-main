import sqlite3
from datetime import datetime


class LongTermMemory:
    def __init__(self, db_path="memory/long_term.db"):
        self.conn = sqlite3.connect(db_path)
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS conversations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            user_input TEXT,
            agent_response TEXT,
            summary TEXT
        )
        """
        self.conn.execute(query)
        self.conn.commit()

    def store(self, user_input, agent_response, summary):
        query = """
        INSERT INTO conversations (timestamp, user_input, agent_response, summary)
        VALUES (?, ?, ?, ?)
        """
        self.conn.execute(query, (
            datetime.utcnow().isoformat(),
            user_input,
            agent_response,
            summary
        ))
        self.conn.commit()

    def fetch_recent(self, limit=5):
        query = """
        SELECT user_input, agent_response, summary
        FROM conversations
        ORDER BY id DESC
        LIMIT ?
        """
        return self.conn.execute(query, (limit,)).fetchall()