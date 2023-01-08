from typing import List
from rterminal.services.redis_svc import redis as r


_TG_SUBSCRIBERS_SET = 'NOTIF_TG_SUBSCRIBERS'


async def add(chat_id: int) -> None:
    await r.sadd(_TG_SUBSCRIBERS_SET, chat_id)


async def get_all() -> List[int]:
    return await r.smembers(_TG_SUBSCRIBERS_SET)


async def is_subscribed(chat_id: int) -> bool:
    return await r.sismember(_TG_SUBSCRIBERS_SET, chat_id)


async def remove(chat_id: int) -> None:
    await r.srem(_TG_SUBSCRIBERS_SET, chat_id)
