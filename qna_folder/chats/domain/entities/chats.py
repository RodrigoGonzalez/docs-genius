from __future__ import annotations

import uuid
from dataclasses import dataclass
from datetime import datetime

from qna.core.events import EventsMixin


@dataclass
class Chats(EventsMixin):
    """Chats entity."""

    id: uuid.UUID
    user_id: uuid.UUID
    session_id: uuid.UUID
    messages: list[str]
    start_time: datetime
    end_time: datetime | None

    def start_conversation(self) -> None:
        """Start the chat conversation."""
        self.start_time = datetime.now()

    def end_conversation(self) -> None:
        """End the chat conversation."""
        self.end_time = datetime.now()

    def add_message(self, message: str) -> None:
        """Add a message to the chat."""
        self.messages.append(message)

    def get_duration(self) -> float | None:
        """Return the duration of the chat in seconds."""
        if self.start_time and self.end_time:
            return (self.end_time - self.start_time).total_seconds()
        return None

    def __repr__(self):
        """Return a string representation of the object."""
        return (
            f"Chats(id={self.id}, "
            f"user_id={self.user_id}, "
            f"session_id={self.session_id}, "
            f"message_len={len(self.messages)}, "
            f"start_time={self.start_time}, "
            f"end_time={self.end_time})"
        )

    def __eq__(self, other):
        """Return True if the objects are equal, False otherwise."""
        return self.__dict__ == other.__dict__
