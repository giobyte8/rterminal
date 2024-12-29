import backoff
import logging
from aiohttp import (
    ClientConnectionError,
    ClientResponseError,
    ClientSession,
)


logger = logging.getLogger(__name__)


_BASE_URL = 'https://api.ipify.org'
_aiohttp_session: ClientSession = None

_RETRYABLE_ERRORS = (
    ClientConnectionError,
    ClientResponseError,
)


def _http() -> ClientSession:
    global _aiohttp_session

    if not _aiohttp_session:
        logger.debug('Creating new aiohttp client session')
        _aiohttp_session = ClientSession()

    return _aiohttp_session


@backoff.on_exception(
    backoff.expo,
    _RETRYABLE_ERRORS,
    max_tries=5
)
async def get_public_ipv4() -> str:
    LOG_ERR_TEMPLATE = '%s error while retrieving public ipv4: %s'

    try:
        async with _http().get(_BASE_URL) as res:
            #logger.debug('GOT REPONSE: %s', res)
            res.raise_for_status()

            if res.status == 200:
                ip = await res.text()

                #logger.debug('Retrieved public ip: %s', ip)
                return ip
            else:
                logger.error(
                    'Non 200 but successful ipfy response: %s',
                    res
                )

    # Catch >= 400 http code errors
    except ClientResponseError as e:
        logger.error(LOG_ERR_TEMPLATE, type(e), e)

        # Retry only on >= 500 http status
        if e.status > 500:
            raise e

    # Catch possible internet failures
    except ClientConnectionError as e:
        logger.error(LOG_ERR_TEMPLATE, type(e), e)
        raise e

    # Any other possible error
    except Exception as e:
        logger.error(LOG_ERR_TEMPLATE, type(e), e)

    # Do we really need explicitly return 'None' (?)
    return None
