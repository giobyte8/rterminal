import os
from dotenv import load_dotenv


load_dotenv()


def ct_api_url() -> str:
    return os.getenv('CT_API_URL', 'http://localhost:3000/api')


def ct_api_key() -> str:
    return os.getenv('CT_API_KEY')


def ct_host_id() -> str:
    return os.getenv('CT_HOST_ID')


def log_level():
    return os.getenv('LOG_LEVEL', 'INFO')