import abc

from qna.core.value_objects import Embedding
from qna.documents.domain.value_objects import EmbeddingId


class DocumentsRepository(abc.ABC):
    """Interface for embeddings repository."""

    @abc.abstractmethod
    def get(self, embedding_id: EmbeddingId) -> Embedding:
        """Get an embedding by id."""

    @abc.abstractmethod
    def save(self, embedding: Embedding) -> None:
        """Save an embedding to the repository."""
