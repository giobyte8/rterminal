from rterminal.services.redis_svc import redis as r


_TG_SUBSCRIBERS_SET = 'NOTIF_TG_SUBSCRIBERS'


async def add(chat_id: int):
    await r.sadd(_TG_SUBSCRIBERS_SET, chat_id)


async def is_subscribed(chat_id: int) -> bool:
    return await r.sismember(_TG_SUBSCRIBERS_SET, chat_id)


async def remove(chat_id: int):
    await r.srem(_TG_SUBSCRIBERS_SET, chat_id)
