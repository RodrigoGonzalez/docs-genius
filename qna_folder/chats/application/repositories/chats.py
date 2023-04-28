import abc

from qna.chats.domain.entities.chats import Chats
from qna.chats.domain.value_objects import ChatsId


class ChatsRepository(abc.ABC):
    """Interface for chats repository."""

    @abc.abstractmethod
    def get(self, chat_id: ChatsId) -> Chats:
        """Get a chat by id."""

    @abc.abstractmethod
    def save(self, chat: Chats) -> None:
        """Save a chat to the repository."""
