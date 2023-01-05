import rterminal.utils.config as cfg
from aiohttp import ClientSession
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
    async with _http().get(f'{ _BASE_URL }/getUpdates', params=p) as res:
        if res.status == 200:
            j_res = await res.json()

            if j_res['ok']:
                return j_res['result']
            else:
                logger.error('Telegram error: %s', j_res['description'])
        else:
            logger.error('HTTP error occurred')


async def send_message(msg: TGResponseMsg):
    url = f'{ _BASE_URL }/sendMessage'
    d = msg.dict()

    async with _http().post(url, data=d) as res:
        if res.status == 200:
            return True
        else:
            logger.error('HTTP error ocurred')
            return False
