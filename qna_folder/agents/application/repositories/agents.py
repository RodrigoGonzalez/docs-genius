import abc

from qna.agents.domain.entities import Agent
from qna.agents.domain.value_objects import AgentID


class AgentsRepository(abc.ABC):
    """Interface for agents repository."""

    @abc.abstractmethod
    def get(self, agent_id: AgentID) -> Agent:
        """Get an agent by id."""

    @abc.abstractmethod
    def save(self, agent: Agent) -> None:
        """Save an agent to the repository."""
