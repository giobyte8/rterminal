import asyncio
import json
import rterminal.utils.config as cfg

from aio_pika import connect
from aio_pika.abc import AbstractIncomingMessage
from pydantic import ValidationError
from rterminal.entities import InfraNotification
from rterminal.msg_senders import tg_msg_sender
from rterminal.utils.rt_logging import logger


_QUEUE_INFRA_NOTIF = 'INFRASTRUCTURE_NOTIFICATIONS'


async def on_message(msg: AbstractIncomingMessage) -> None:
    logger.info('Infrastructure notification received')
    logger.debug('Infra notif body: %s', msg.body.decode('utf-8'))

    try:
        j_notif = json.loads(msg.body)
        notif = InfraNotification(**j_notif)

        await tg_msg_sender.infra_notification(notif)
    except ValidationError as e:
        logger.error(e)
    except json.JSONDecodeError:
        logger.error(
            'Received notification is not a valid json: %s',
            msg.body
        )

    await msg.ack()


async def start() -> None:
    conn_url = (
        f'amqp://{ cfg.rabbitmq_user() }:{ cfg.rabbitmq_pass() }@'
        f'{ cfg.rabbitmq_host() }:{ cfg.rabbitmq_port() }/'
    )

    logger.debug('Connecting to rabbitmq')
    conn = await connect(conn_url)
    async with conn:
        channel = await conn.channel()
        queue = await channel.declare_queue(_QUEUE_INFRA_NOTIF)

        await queue.consume(on_message)
        logger.info('Listening for infrastructure notifications')

        await asyncio.Future()
