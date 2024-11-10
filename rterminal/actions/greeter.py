import logging
from .base import Action


logger = logging.getLogger(__name__)


class GreeterAction(Action):
    def run(self) -> None:
        logger.info('Hello, World!')
