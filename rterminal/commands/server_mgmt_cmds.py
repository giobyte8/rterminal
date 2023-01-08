from rterminal.entities import (
    TGChat,
    TGResponseMsg
)
from rterminal.api_clients import ipfy_api


async def public_ip(chat: TGChat) -> TGResponseMsg:
    ip = await ipfy_api.get_ip()

    return TGResponseMsg(
        chat_id=chat.id,
        text=f'Public ip: { ip }'
    )
