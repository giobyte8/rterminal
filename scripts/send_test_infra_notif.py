import asyncio
import json
import os

from aio_pika import Message, connect
from dotenv import load_dotenv


_QUEUE_INFRA_NOTIF = 'INFRASTRUCTURE_NOTIFICATIONS'
load_dotenv()


async def main() -> None:
    url = (
        f'amqp://{ os.getenv("RABBITMQ_USER") }:{ os.getenv("RABBITMQ_PASS") }@'
        f'{ os.getenv("RABBITMQ_HOST") }:{ os.getenv("RABBITMQ_PORT") }/'
    )
    connection = await connect(url)

    async with connection:
        channel = await connection.channel()
        queue = await channel.declare_queue(_QUEUE_INFRA_NOTIF)

        msg = {
            'level': 'MEDIUM',
            'message': 'This is a test notification 👨🏻‍💻'
        }

        print('[x] Publishing test infrastructure notification to rabbitmq')
        await channel.default_exchange.publish(
            Message(json.dumps(msg).encode('utf-8')),
            routing_key=queue.name,
        )

        print(" [->] Notif was sent")


if __name__ == "__main__":
    asyncio.run(main())
