from pydantic import ValidationError
from rterminal import tg_api
from rterminal.entities import TGMessage
from rterminal.errors import UnprocessableTelegramUpdateError
from rterminal.services import conversation_svc
from rterminal.utils.rt_logging import logger


_highest_rec_update = 975271545


def start():
    """Keeps polling telegram API for updates
    """

    updates = tg_api.getUpdates(_highest_rec_update + 1)
    for update in updates:
        try:
            # print(update)
            on_update(update)
        except UnprocessableTelegramUpdateError as err:
            logger.error('Unknown telegram update. %s. %s', err, update)
        except ValidationError as err:
            logger.error('Telegram update parsing error: %s', err.json())


def on_update(update: dict):
    update_id = update['update_id']
    logger.info('Update received: %s', update_id)

    # Update the highest received update to use it as
    # offset in next request
    global _highest_rec_update
    _highest_rec_update = max(_highest_rec_update, update_id)

    # Proccess update as a message
    if 'message' not in update:
        raise UnprocessableTelegramUpdateError('"message" element not found')
    message = TGMessage(**update['message'])

    conversation_svc.on_message(message)
