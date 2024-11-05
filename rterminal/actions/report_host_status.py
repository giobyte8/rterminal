import logging
from .base import Action
from rterminal.clients import ipfy_api as ipfy


logger = logging.getLogger(__name__)


class ReportHostStatusAction(Action):

    async def run(self) -> None:
        logger.debug('Reporting host status')

        ip = await ipfy.get_public_ipv4()
        logger.debug(f'Public IPv4: { ip }')