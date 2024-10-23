from .jobs.greeter import GreeterJob
from .scheduler.aio_scheduler import AIOScheduler


async def start() -> None:
    job1 = GreeterJob()

    scheduler = AIOScheduler()
    await scheduler.add_job(job1, 3)
    await scheduler.start()
