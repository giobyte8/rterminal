import logging
from aiohttp import (
    ClientError,
    ClientConnectionError,
    ClientResponseError,
    ClientSession,
)


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
    # TODO Implement exponential backoff retries

    try:
        async with _http().get(_BASE_URL) as res:
            res.raise_for_status()

            if res.status == 200:
                ip = await res.text()

                logger.debug('Retrieved public ip: %s', ip)
                return ip
            else:
                # TODO Handle non 200 successful responses
                # TODO   Verify official docs for possible responses
                logger.error('IPFY_API: HTTP error ocurred')

    # Catch >= 400 http code errors
    except ClientResponseError as e:
        if e.status > 500:
            # TODO: Exp backoff retry
            pass
        else:
            # TODO: Log error and don't retry
            pass

    # Catch possible internet failures
    except ClientConnectionError as e:
        # TODO Log error and retry
        pass

    # Other possible client errors
    except ClientError as e:
        # TODO Log error and don't retry
        pass

    except Exception as e:
        # TODO Log and don't retry
        pass
