from __future__ import annotations

from agents import SessionABC, TResponseInputItem


class PostgresSession(SessionABC):
    """PostgreSQL-based implementation of session storage for OpenAI Agents.

    This implementation stores conversation history in a PostgreSQL database,
    mirroring the behavior of the SQLiteSession implementation in the Agents SDK.

    See here: https://github.com/openai/openai-agents-python/blob/main/src/agents/memory/sqlite_session.py
    """

    def __init__(self, session_id: str, database_url: str) -> None:
        """Initialize the Postgres session.

        Args:
            session_id: Unique identifier for the conversation session.
            database_url: SQLAlchemy-compatible database URL pointing to PostgreSQL.
        """
        self.session_id = session_id
        self._database_url = database_url

    async def get_items(self, limit: int | None = None) -> list["TResponseInputItem"]:
        """Retrieve the conversation history for this session."""
        raise NotImplementedError

    async def add_items(self, items: list["TResponseInputItem"]) -> None:
        """Add new items to the conversation history."""
        raise NotImplementedError

    async def pop_item(self) -> "TResponseInputItem | None":
        """Remove and return the most recent item from the session."""
        raise NotImplementedError

    async def clear_session(self) -> None:
        """Clear all items for this session."""
        raise NotImplementedError
