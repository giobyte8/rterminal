from abc import ABCMeta, abstractmethod
from ..base import Action


class Scheduler(metaclass=ABCMeta):

    @abstractmethod
    async def add(self, action: Action, every_seconds: int) -> None:
        """Adds an 'Action' to this scheduler to be executed
        according to given interval once scheduler is started.

        Args:
            action (Action): Task to schedule for execution
            every_seconds (int): Action will be executed every
                given number of seconds
        """

    @abstractmethod
    async def start(self) -> None:
        """Starts this scheduler, which means that actions
        execution begins"""