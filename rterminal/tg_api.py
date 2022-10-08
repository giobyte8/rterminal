import requests
import rterminal.config as cfg
from rterminal.rt_logging import logger

_BASE_URL  = f'https://api.telegram.org/bot{ cfg.tg_bot_token() }'


def getMe():
    res = requests.get(f'{ _BASE_URL }/getMe')
    return res.json()

def getUpdates():
    try:
        logger.debug('Retrieving updates from telegram API')
        res = requests.get(f'{ _BASE_URL }/getUpdates')

        res.raise_for_status()
        j_res = res.json()

        if j_res['ok']:
            return j_res['result']
        else:
            logger.error('Telegram error: %s', j_res['description'])
    except requests.HTTPError as err:
        logger.error('HTTP error occurred: %s', err)
    except Exception as err:
        logger.error('Error while retrieving updates: %s', err)
