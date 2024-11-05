from abc import ABCMeta, abstractmethod


class Action(metaclass=ABCMeta):

    @abstractmethod
    async def run(self) -> None:
        """Executes this action
        """
