from __future__ import annotations

from abc import ABC
from typing import Any

from qna.agents.domain.entities.text_code_processor import TextCodeProcessor
from qna.agents.domain.value_objects import AgentID


class Agent(TextCodeProcessor, ABC):
    """
    Base class for agents.

    - Implement the methods from TextCodeProcessor
    """

    def __init__(
        self, agent_id: AgentID, api_key: str, model_name: str, config: dict[str, Any] | None = None
    ):
        """
        Initialize an agent.

        Parameters
        ----------
        agent_id : AgentID
            Unique identifier for the agent.
        api_key : str

        model_name : str
            Name of the language model.
        config : Optional[Dict[str, Any]]
            Configuration parameters for the agent.
        """
        self.agent_id = agent_id
        self.api_key = api_key
        self.model_name = model_name
        self.config = config if config else {}

    def preprocess_text(self, text: str, **kwargs) -> str:
        """
        Preprocess text.

        Parameters
        ----------
        text
        kwargs

        Returns
        -------

        """
        # Implement text preprocessing logic

    def complete_text(self, prompt: str, **kwargs) -> str:
        """
        Implement text completion logic using the language model API

        Parameters
        ----------
        prompt
        kwargs

        Returns
        -------

        """

    def complete_chat(self, conversation: list[dict[str, str]], **kwargs) -> str:
        """
        Implement chat completion logic using the language model API

        Parameters
        ----------
        conversation
        kwargs

        Returns
        -------

        """

    def summarize(self, text: str, **kwargs) -> str:
        """
        Implement summarization logic using the language model API

        Parameters
        ----------
        text
        kwargs

        Returns
        -------

        """

    def generate_embeddings(self, text: str, **kwargs) -> list[float]:
        """
        Implement embedding generation logic using the language model API

        Parameters
        ----------
        text
        kwargs

        Returns
        -------

        """

    def generate_text(self, prompt: str, **kwargs) -> str:
        """
        Implement text generation logic using the language model API

        Parameters
        ----------
        prompt
        kwargs

        Returns
        -------

        """

    def classify_text(self, text: str, **kwargs) -> str:
        """
        Implement text classification logic using the language model API

        Parameters
        ----------
        text
        kwargs

        Returns
        -------

        """
