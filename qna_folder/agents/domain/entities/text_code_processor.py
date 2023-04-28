from abc import ABC
from abc import abstractmethod
from typing import Any


class TextCodeProcessor(ABC):
    """Interface for text and code processing agents."""

    @abstractmethod
    def preprocess_text(self, text: str, **kwargs) -> str:
        """Preprocess text."""

    @abstractmethod
    def evaluate_code(self, code: str, **kwargs) -> Any:
        """Evaluate code."""

    @abstractmethod
    def improve_code(self, code: str, **kwargs) -> str:
        """Improve code."""

    @abstractmethod
    def generate_code(self, prompt: str, **kwargs) -> str:
        """Generate code."""

    @abstractmethod
    def improve_text(self, text: str, **kwargs) -> str:
        """Improve text."""
