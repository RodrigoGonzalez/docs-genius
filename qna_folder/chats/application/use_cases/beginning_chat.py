from dataclasses import dataclass
from datetime import datetime

from qna.chats.application.repositories import ChatsRepository
from qna.chats.domain.entities import Chats
from qna.chats.domain.value_objects import ChatsId


@dataclass
class BeginningChatsInputDto:
    """Input DTO for beginning a chat.""" ""

    chats_id: ChatsId
    title: str
    ends_at: datetime


class BeginningChat:
    def __init__(self, chats_repo: ChatsRepository) -> None:
        self.chats_repo = chats_repo

    def start_conversation(self, input_dto: BeginningChatsInputDto) -> None:
        """Start a chat conversation."""

        auction = Chats.start_conversation(
            input_dto.chats_id, input_dto.title, input_dto.starting_price, input_dto.ends_at
        )
        self.chats_repo.save(auction)
