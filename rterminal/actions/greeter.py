from .base import Action


class GreeterAction(Action):
    def run(self) -> None:
        logger.info('Hello, World!')
