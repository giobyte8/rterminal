from rterminal.entities import (
    ConversationStatus,
    TGChat,
    TGMessage,
    TGResponseMsg
)
from rterminal.services import auth_svc
from rterminal.services import cache_svc


def start(chat: TGChat) -> TGResponseMsg:
    msg_txt = (
        f'Hey { chat.first_name }! Nice to see you here. '
        'What\'s the passphrase?'
    )

    cache_svc.set_conversation_status(
        chat.id,
        ConversationStatus.WAITING_USER_PASSPHRASE
    )
    return TGResponseMsg(chat_id=chat.id, text=msg_txt)


def on_reauthentication_required(chat_id: int) -> TGResponseMsg:
    txt = 'Hey! it\'s been a while.\nWhat\'s the passphrase again?'
    cache_svc.set_conversation_status(
        chat_id,
        ConversationStatus.WAITING_USER_PASSPHRASE
    )
    return TGResponseMsg(chat_id=chat_id, text=txt)


def on_user_passphrase(msg: TGMessage) -> TGResponseMsg:
    cache_svc.set_conversation_status(msg.chat.id, ConversationStatus.STANDBY)

    if auth_svc.checkpw(msg.text):
        cache_svc.add_tg_authorized_chat(msg.chat.id)
        return TGResponseMsg(
            chat_id=msg.chat.id,
            text='Cool! You can enter commands now')
    else:
        msg_txt = 'No! What are you doing?'
        return TGResponseMsg(chat_id=msg.chat.id, text=msg_txt)


def ping(chat: TGChat):
    return TGResponseMsg(chat_id=chat.id, text='Hey! I\'m here')
