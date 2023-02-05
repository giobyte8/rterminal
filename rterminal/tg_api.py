import asyncio
import rterminal.utils.config as cfg
from aiohttp import ClientSession
from aiohttp import client_exceptions as aiohttp_ex
from rterminal.entities import TGResponseMsg
from rterminal.utils.rt_logging import logger

_BASE_URL  = f'https://api.telegram.org/bot{ cfg.tg_bot_token() }'
_aiohttp_session: ClientSession = None

def _http() -> ClientSession:
    global _aiohttp_session

    if not _aiohttp_session:
        logger.debug('TG_API: Creating new aiohttp client session')
        _aiohttp_session = ClientSession()

    return _aiohttp_session


async def close_http_session():
    global _aiohttp_session

    if _aiohttp_session:
        await _aiohttp_session.close()


async def getMe():
    async with _http().get(f'{ _BASE_URL }/getMe') as res:
        return await res.json()


async def get_updates(offset: int):
    # logger.debug('Retrieving updates from telegram API')
    p = { 'offset': offset }

    try:
        async with _http().get(f'{ _BASE_URL }/getUpdates', params=p) as res:
            if res.status == 200:
                j_res = await res.json()

                if j_res['ok']:
                    return j_res['result']
                else:
                    logger.error('Telegram error: %s', j_res['description'])
            else:
                logger.error('HTTP error occurred')
    except aiohttp_ex.ClientOSError as e:
        logger.warn('aiohttp error: %s', e)
        await asyncio.sleep(3)
    except Exception as e:
        logger.error('Error while retrieving telegram updates: %s', e)
        await asyncio.sleep(3)

    # In case error ocurred, return empty array of updates
    return []



async def send_message(msg: TGResponseMsg):
    url = f'{ _BASE_URL }/sendMessage'
    d = msg.dict()

    async with _http().post(url, data=d) as res:
        if res.status == 200:
            return True
        else:
            logger.error('HTTP error ocurred')
            return False
