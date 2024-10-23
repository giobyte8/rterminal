from abc import ABCMeta, abstractmethod


class Job(metaclass=ABCMeta):

    @abstractmethod
    def run(self) -> None:
        """Executes this job
        """
