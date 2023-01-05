from typing import List
from rterminal import tg_api
from rterminal.commands import (
    notifications_cmd,
    setup_cmds
)
from rterminal.entities import (
    ConversationStatus,
    TGChat,
    TGMessage
)
from rterminal.services import cache_svc


async def on_message(msg: TGMessage):
    msg_txt = msg.text

    # Check if message is a command
    if msg_txt.startswith('/'):
        words = msg_txt.split()
        command = words[0][1:]
        args = None

        if len(words) > 1:
            words.pop(0)
            args = words

        await on_command(msg.chat, command, args)

    # On raw message
    else:
        conv_status = await cache_svc.get_conversation_status(msg.chat.id)

        if conv_status == ConversationStatus.WAITING_USER_PASSPHRASE:
            res_msg = await setup_cmds.on_user_passphrase(msg)
            await tg_api.send_message(res_msg)

        else:
            # TODO Return a 'What?' and suggest some basic commands
            print(f'id: { msg.chat.id } Message: { msg }')


async def on_command(chat: TGChat, command: str, args: List[str]):
    res_msg = None

    # 'start' does not requires previous authentication
    if command == 'start':
        res_msg = await setup_cmds.start(chat)

    # Check for chat authorization
    elif await cache_svc.is_tg_chat_authorized(chat.id):
        if command == 'ping':
            res_msg = setup_cmds.ping(chat)

        if command == 'notifications':
            res_msg = await notifications_cmd.run(chat, args)

    # Ask for passphrase again
    else:
        res_msg = await setup_cmds.on_reauthentication_required(chat.id)

    if res_msg:
        await tg_api.send_message(res_msg)
