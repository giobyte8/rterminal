import os
from dotenv import load_dotenv

load_dotenv()


def tg_bot_token():
    return os.getenv('TG_BOT_TOKEN')


def runtime_path():
    return os.getenv('RUNTIME_PATH')


def logs_path():
    return os.path.join(runtime_path(), 'logs')


def log_level():
    return os.getenv('LOG_LEVEL', 'error')
