from .greeter import GreeterAction
from .report_host_status import ReportHostStatusAction
from .scheduler.aio_scheduler import AIOScheduler


async def start() -> None:
    job1 = GreeterAction()
    job2 = ReportHostStatusAction()

    scheduler = AIOScheduler()
    await scheduler.add(job1, 3)
    await scheduler.add(job2, 5)
    await scheduler.start()
