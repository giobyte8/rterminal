from .base import Job


class GreeterJob(Job):
    def run(self) -> None:
        print("Hello, World!")
