from pydantic import ValidationError
from rterminal import tg_api
from rterminal.entities import TGMessage
from rterminal.errors import UnprocessableTelegramUpdateError
from rterminal.services import conversation_svc
from rterminal.utils.rt_logging import logger


_highest_rec_update = 0


def start():
    """Keeps polling telegram API for updates
    """

    try:
        logger.info('Starting telegram updates listener')

        while True:
            updates = tg_api.getUpdates(_highest_rec_update + 1)
            for update in updates:
                try:
                    on_update(update)
                except UnprocessableTelegramUpdateError as err:
                    logger.error('Unknown telegram update. %s. %s', err, update)
                except ValidationError as err:
                    logger.error('Telegram update parsing error: %s', err.json())
    except KeyboardInterrupt:
        logger.info('Shutting down telegram updates listener...')


def on_update(update: dict):
    update_id = update['update_id']
    logger.info('Update received: %s', update_id)
    logger.debug('Update body: %s', update)

    # Update the highest received update to use it as
    # offset in next request
    global _highest_rec_update
    _highest_rec_update = max(_highest_rec_update, update_id)

    # Verify that update is a new message
    if 'message' not in update:
        raise UnprocessableTelegramUpdateError('"message" element not found')

    # Process as a message
    message = TGMessage(**update['message'])
    conversation_svc.on_message(message)
