import abc

from qna.core.value_objects import Document
from qna.documents.domain.value_objects import DocumentId


class DocumentsRepository(abc.ABC):
    """Interface for documents repository."""

    @abc.abstractmethod
    def get(self, document_id: DocumentId) -> Document:
        """Get a document by id."""

    @abc.abstractmethod
    def save(self, document: Document) -> None:
        """Save a document to the repository."""
