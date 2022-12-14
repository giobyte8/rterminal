import rterminal.utils.config as cfg
from rterminal.services.redis_svc import redis as r
from rterminal.entities import ConversationStatus
from rterminal.utils.rt_logging import logger


_TG_AUTH_CHATS_PREFIX = 'TG_AUTHORIZED_CHAT'
_TG_CONVERSATION_STATUS = 'TG_CONVERSATION_STATUS'


async def is_tg_chat_authorized(chat_id: int) -> bool:
    key = f'{ _TG_AUTH_CHATS_PREFIX }:{ chat_id }'

    # exists works more like a 'count'
    return await r.exists(key) == 1


async def add_tg_authorized_chat(chat_id: int):
    key = f'{ _TG_AUTH_CHATS_PREFIX }:{ chat_id }'
    await r.set(key, 'Authenticated', cfg.session_expire())


async def set_conversation_status(chat_id: int, status: ConversationStatus):
    await r.hset(_TG_CONVERSATION_STATUS, chat_id, status.value)


async def get_conversation_status(chat_id) -> ConversationStatus:
    status = await r.hget(_TG_CONVERSATION_STATUS, chat_id)
    if not status:
        return ConversationStatus.UNKNOWN

    try:
        return ConversationStatus[status.decode('UTF-8')]
    except KeyError:
        logger.warn(
            'Wrong conversation status: chat_id: %s, status: %s',
            chat_id,
            status)
        return ConversationStatus.UNKNOWN
