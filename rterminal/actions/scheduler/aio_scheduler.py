from apscheduler.schedulers.asyncio import AsyncIOScheduler
from .base import Scheduler
from ..base import Action


class AIOScheduler(Scheduler):
    """Leverages apscheduler 3.x library and asyncio for workers.
    Actions live in memory, no persistent storage is used
    """

    def __init__(self):
        self._scheduler = AsyncIOScheduler()

    async def add(self, action: Action, every_seconds: int) -> None:
        self._scheduler.add_job(
            action.run,
            'interval',
            seconds=every_seconds
        )

    async def start(self):
        self._scheduler.start()
