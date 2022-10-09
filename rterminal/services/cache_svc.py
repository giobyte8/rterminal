import redis
import rterminal.utils.config as cfg
from rterminal.entities import ConversationStatus
from rterminal.utils.rt_logging import logger


_TG_AUTH_CHATS_PREFIX = 'TG_AUTHORIZED_CHAT'
_TG_CONVERSATION_STATUS = 'TG_CONVERSATION_STATUS'
r = redis.Redis(cfg.redis_host(), cfg.redis_port())


def is_tg_chat_authorized(chat_id: int) -> bool:
    key = f'{ _TG_AUTH_CHATS_PREFIX }:{ chat_id }'

    # exists works more like a 'count'
    return r.exists(key) == 1


def add_tg_authorized_chat(chat_id: int):
    key = f'{ _TG_AUTH_CHATS_PREFIX }:{ chat_id }'
    r.set(key, 'Authenticated', cfg.session_expire())


def set_conversation_status(chat_id: int, status: ConversationStatus):
    r.hset(_TG_CONVERSATION_STATUS, chat_id, status.value)


def get_conversation_status(chat_id) -> ConversationStatus:
    status = r.hget(_TG_CONVERSATION_STATUS, chat_id)
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
