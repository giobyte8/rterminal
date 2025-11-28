import logging
import requests
from ..utils import config as cfg


log = logging.getLogger(__name__)


def notify(msg: str) -> None:
    url = f'{cfg.ct_api_url()}/notifications'
    headers = {
        'Authorization': f'Bearer {cfg.ct_api_key()}',
        'Content-Type': 'application/json'
    }
    payload = {
        'title': 'rterminal > boot',
        'content': msg
    }

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        if response.status_code >= 200 and response.status_code < 300:
            log.debug('Notification sent successfully.')
        else:
            log.warning(f'Notification POST status code: {response.status_code}')
            response.raise_for_status()

    except requests.exceptions.HTTPError as http_err:
        status_code  = getattr(http_err.response, "status_code", None)
        response_txt = getattr(http_err.response, "text", None)
        log.error(
            'HTTP error occurred - '
            f'Status code: { status_code } - '
            f'Response: { response_txt } - '
            f'Error: {http_err}'
        )
    except requests.exceptions.Timeout as timeout_err:
        log.error(f'Timeout error occurred: {timeout_err}')
    except requests.exceptions.RequestException as req_err:
        log.error(f'Request exception occurred: {req_err}')
    except Exception as err:
        log.error(f'Unexpected error occurred: {err}')


def update_host_status(ipv4_public: str) -> None:
    host_id = cfg.ct_host_id()
    url = f'{ cfg.ct_api_url() }/hosts/{ host_id }/status'

    headers = {
        'Authorization': f'Bearer {cfg.ct_api_key()}',
        'Content-Type': 'application/json'
    }
    payload = {
        'ipv4Public': ipv4_public
    }

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        if response.status_code >= 200 and response.status_code < 300:
            log.debug('Host status update sent successfully.')
        else:
            log.warning(
                f'Host status update response code: {response.status_code}'
            )
            response.raise_for_status()

    except requests.exceptions.HTTPError as http_err:
        status_code  = getattr(http_err.response, "status_code", None)
        response_txt = getattr(http_err.response, "text", None)
        log.error(
            'HTTP error occurred - '
            f'Status code: { status_code } - '
            f'Response: { response_txt } - '
            f'Error: {http_err}'
        )
    except requests.exceptions.Timeout as timeout_err:
        log.error(f'Timeout error occurred: {timeout_err}')
    except requests.exceptions.RequestException as req_err:
        log.error(f'Request exception occurred: {req_err}')
    except Exception as err:
        log.error(f'Unexpected error occurred: {err}')