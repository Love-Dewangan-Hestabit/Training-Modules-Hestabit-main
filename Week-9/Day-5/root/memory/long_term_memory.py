
import os
import sqlite3
from datetime import datetime

IMPORTANCE_THRESHOLD = 5


class LongTermMemory:
    def __init__(self, db_path: str = "memory/long_term.db"):
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self._create_table()

    def _create_table(self) -> None:
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS conversations (
                id               INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp        TEXT    NOT NULL,
                user_task        TEXT    NOT NULL,
                agent_response   TEXT    NOT NULL,
                summary          TEXT    NOT NULL,
                tools_used       TEXT    DEFAULT '',
                importance_score INTEGER DEFAULT 5
            )
        """)
        self.conn.commit()

    def store(
        self,
        user_task: str,
        agent_response: str,
        summary: str,
        tools_used: str = "",
        importance_score: int = 5,
    ) -> bool:
        """
        Store a conversation only if importance >= threshold.
        Returns True if stored, False if skipped.
        """
        if importance_score < IMPORTANCE_THRESHOLD:
            return False

        self.conn.execute(
            """
            INSERT INTO conversations
                (timestamp, user_task, agent_response, summary, tools_used, importance_score)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                datetime.utcnow().isoformat(),
                user_task,
                agent_response[:2000], 
                summary,
                tools_used,
                importance_score,
            ),
        )
        self.conn.commit()
        return True

    def fetch_recent(self, limit: int = 5) -> list[tuple]:
        """Fetch the most recent stored conversations."""
        return self.conn.execute(
            """
            SELECT user_task, summary, tools_used, importance_score
            FROM conversations
            ORDER BY id DESC
            LIMIT ?
            """,
            (limit,),
        ).fetchall()

    def count(self) -> int:
        row = self.conn.execute("SELECT COUNT(*) FROM conversations").fetchone()
        return row[0] if row else 0

    def close(self) -> None:
        self.conn.close()
