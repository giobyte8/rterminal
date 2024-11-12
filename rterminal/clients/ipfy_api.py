import logging
from aiohttp import ClientSession


logger = logging.getLogger(__name__)


_BASE_URL = 'https://api.ipify.org'
_aiohttp_session: ClientSession = None


def _http() -> ClientSession:
    global _aiohttp_session

    if not _aiohttp_session:
        logger.debug('Creating new aiohttp client session')
        _aiohttp_session = ClientSession()

    return _aiohttp_session


async def get_public_ipv4() -> str:
    # TODO Implement error handling and retry
    async with _http().get(_BASE_URL) as res:
        if res.status == 200:
            ip = await res.text()

            logger.debug('Retrieved public ip: %s', ip)
            return ip
        else:
            logger.error('IPFY_API: HTTP error ocurred')
