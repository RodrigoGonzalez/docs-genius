from dataclasses import dataclass

from qna.chats.application.repositories.chats import ChatsRepository
from qna.chats.domain.value_objects import ChatsId


@dataclass
class EndingChatInputDto:
    """Input DTO for ending chat use case."""

    chat_id: ChatsId


class EndingChatOutputDto:
    """Output DTO for ending chat use case."""

    def __init__(self, chat_repo: ChatsRepository):
        self.chat_repo = chat_repo

    def execute(self, input_dto: EndingChatInputDto) -> None:
        chat = self.chat_repo.get(input_dto.chat_id)
        # ???
        self.chat_repo.save(chat)
