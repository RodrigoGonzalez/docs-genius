import abc
from dataclasses import dataclass
from datetime import datetime

from foundation.value_objects import Money
from qna.chats.domain.value_objects import ChatsId


@dataclass
class ChatsDto:
    """Chats DTO."""

    id: int
    title: str
    current_price: Money
    starting_price: Money
    ends_at: datetime


class GetSingleChat(abc.ABC):
    """Interface for getting a single chat."""

    @abc.abstractmethod
    def query(self, chat_id: ChatsId) -> ChatsDto:
        """Return a single chat."""


class GetActiveChats(abc.ABC):
    """Interface for getting active chats."""

    @abc.abstractmethod
    def query(self) -> list[ChatsDto]:
        """Return a list of active chats."""
