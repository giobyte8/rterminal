import os
from dotenv import load_dotenv

load_dotenv()


def tg_bot_token():
    return os.getenv('TG_BOT_TOKEN')


def bot_auth_hash():
    return os.getenv('BOT_AUTH_HASH')


def redis_host():
    return os.getenv('REDIS_HOST')


def redis_port():
    return os.getenv('REDIS_PORT')


def runtime_path():
    return os.getenv('RUNTIME_PATH')


def logs_path():
    return os.path.join(runtime_path(), 'logs')


def log_level():
    return os.getenv('LOG_LEVEL', 'error')
