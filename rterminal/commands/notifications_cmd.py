from typing import List
from rterminal.entities import (
    TGChat,
    TGResponseMsg
)
from rterminal.services import notif_subs_svc


class SubCmd:
    SUBSCRIBE = 'subscribe'
    UNSUBSCRIBE = 'unsubscribe'
    HELP = 'help'


async def run(chat: TGChat, args: List[str]) -> TGResponseMsg:
    if not args:
        return _make_usage_msg(chat)

    subcmd = args.pop(0)
    if subcmd == SubCmd.SUBSCRIBE:
        return await _on_subscribe(chat)
    elif subcmd == SubCmd.UNSUBSCRIBE:
        return await _on_unsubscribe(chat)
    else:
        return _make_usage_msg(chat)


async def _on_subscribe(chat: TGChat) -> TGResponseMsg:
    if await notif_subs_svc.is_subscribed(chat.id):
        t = 'You\'re already subscribed to notifications'
        return TGResponseMsg(chat_id=chat.id, text=t)

    else:
        await notif_subs_svc.add(chat.id)
        return TGResponseMsg(
            chat_id=chat.id,
            text='You\'re now susbcribed to notifications'
        )


async def _on_unsubscribe(chat: TGChat) -> TGResponseMsg:
    if await notif_subs_svc.is_subscribed(chat.id):
        await notif_subs_svc.remove(chat.id)
        return TGResponseMsg(
            chat_id=chat.id,
            text='You\'re now unsubscribed from notifications')

    else:
        return TGResponseMsg(
            chat_id=chat.id,
            text='You\'re not subscribed to notifications 🧐'
        )


def _make_usage_msg(chat: TGChat) -> TGResponseMsg:
    help = (
        'The /notifications command requires one of following subcommands: \n'
        f' - { SubCmd.SUBSCRIBE } \n'
        f' - { SubCmd.UNSUBSCRIBE } \n'
    )

    return TGResponseMsg(chat_id=chat.id, text=help)
