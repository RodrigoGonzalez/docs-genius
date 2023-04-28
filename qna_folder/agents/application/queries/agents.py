import abc
from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from foundation.value_objects import Money


@dataclass
class AgentDto:
    """Data transfer object for an agent."""

    agent_id: UUID
    role: str
    model_name: str
    current_price: Money
    starting_price: Money
    start_at: datetime
    ends_at: datetime


class GetSingleAgent(abc.ABC):
    """Get a single agent by id."""

    @abc.abstractmethod
    def query(self, agent_id: UUID) -> AgentDto:
        """
        Get a single agent by id.

        Parameters
        ----------
        agent_id : UUID

        Returns
        -------
        AgentDto
            Agent data transfer object.
        """


class GetActiveAgents(abc.ABC):
    """Get all active agents."""

    @abc.abstractmethod
    def query(self) -> list[AgentDto]:
        """Query all active agents."""
