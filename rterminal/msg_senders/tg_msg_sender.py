from rterminal import tg_api
from rterminal.entities import (
    InfraNotification,
    InfraNotifLevel,
    TGResponseMsg
)
from rterminal.services import notif_subs_svc
from rterminal.utils.rt_logging import logger


async def infra_notification(notif: InfraNotification) -> None:
    subscribers = await notif_subs_svc.get_all()
    for sub in subscribers:

        # Chat id is stored as bytes in redis set
        chat_id = int(sub.decode('utf-8'))
        tg_msg = _make_infra_notif_msg(chat_id, notif)

        await tg_api.send_message(tg_msg)
        logger.debug('Infra notif send by telegram to chat %s', chat_id)


def _make_infra_notif_msg(
    chat_id: int,
    notif: InfraNotification
) -> TGResponseMsg:

    icon = '🔵'
    if notif.level == InfraNotifLevel.MEDIUM:
        icon = '🟠'
    elif notif.level == InfraNotifLevel.HIGH:
        icon = '🔴'

    return TGResponseMsg(
        chat_id=chat_id,
        text=f'{ icon } { notif.message }'
    )
