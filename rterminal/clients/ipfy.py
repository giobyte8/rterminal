import logging
import requests


log = logging.getLogger(__name__)
_BASE_URL = 'https://api.ipify.org'


def get_public_ip() -> str | None:
    """Fetch the public IP address using the ipfy service.

    Returns:
        str | None: The public IP address as a string, or None if an error occurs.
    """

    try:
        response = requests.get(_BASE_URL, timeout=10)
        response.raise_for_status()
        ip_address = response.text

        log.debug(f'Fetched public IP address: { ip_address }')
        return ip_address

    except requests.exceptions.HTTPError as http_err:
        status_code  = getattr(http_err.response, "status_code", None)
        response_txt = getattr(http_err.response, "text", None)
        log.error(
            'HTTP error occurred while fetching public IP - '
            f'Status code: { status_code } - '
            f'Response: { response_txt } - '
            f'Error: {http_err}'
        )
    except requests.exceptions.Timeout as timeout_err:
        log.error(f'Timeout error occurred while fetching public IP: {timeout_err}')
    except requests.exceptions.RequestException as req_err:
        log.error(f'Request exception occurred while fetching public IP: {req_err}')
    except Exception as err:
        log.error(f'Unexpected error occurred while fetching public IP: {err}')

    return None
