from aiohttp import ClientSession
from rterminal.utils.rt_logging import logger


_BASE_URL = 'https://api.ipify.org'
_aiohttp_session: ClientSession = None


def _http() -> ClientSession:
    global _aiohttp_session

    if not _aiohttp_session:
        logger.debug('IPFY_API: Creating new aiohttp client session')
        _aiohttp_session = ClientSession()

    return _aiohttp_session


async def get_ip() -> str:
    async with _http().get(_BASE_URL) as res:
        if res.status == 200:
            ip = await res.text()

            logger.info('Retrieved public ip: %s', ip)
            return ip
        else:
            logger.error('IPFY_API: HTTP error ocurred')
