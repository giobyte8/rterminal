from abc import ABCMeta, abstractmethod
from ..jobs.base import Job


class Scheduler(metaclass=ABCMeta):

    @abstractmethod
    async def add_job(self, job: Job, every_seconds: int) -> None:
        """Adds a 'Job' to this scheduler to be executed according
        to given interval once scheduler is started.

        Args:
            job (Job): Task to schedule for execution
            every_seconds (int): Job will be executed every given number
                of seconds
        """

    @abstractmethod
    async def start(self) -> None:
        """Starts this scheduler, which means that jobs
        execution begins"""