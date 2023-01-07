import asyncio
from pydantic import ValidationError
from rterminal import tg_api
from rterminal.entities import TGMessage
from rterminal.errors import UnprocessableTelegramUpdateError
from rterminal.services import conversation_svc
from rterminal.utils.rt_logging import logger


_highest_rec_update = 0


async def start():
    """Keeps polling telegram API for updates
    """

    try:
        logger.info('Listening for telegram updates')

        while True:
            updates = await tg_api.get_updates(_highest_rec_update + 1)
            for update in updates:
                try:
                    await on_update(update)
                except UnprocessableTelegramUpdateError as err:
                    logger.error('Unknown telegram update. %s. %s', err, update)
                except ValidationError as err:
                    logger.error('Telegram update parsing error: %s', err.json())
    except KeyboardInterrupt:
        logger.info('Shutting down telegram updates listener...')
        await tg_api.close_http_session()


async def on_update(update: dict):
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
    await conversation_svc.on_message(message)
