from apscheduler.schedulers.asyncio import AsyncIOScheduler
from .base import Scheduler
from ..jobs.base import Job


class AIOScheduler(Scheduler):
    """Leverages apscheduler 3.x library and asyncio for workers.
    Jobs live in memory, no persistent storage is used
    """

    def __init__(self):
        self._scheduler = AsyncIOScheduler()

    async def add_job(self, job: Job, every_seconds: int) -> None:
        self._scheduler.add_job(
            job.run,
            'interval',
            seconds=every_seconds
        )

    async def start(self):
        self._scheduler.start()
