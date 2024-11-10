import logging
#import os

from logging.handlers import RotatingFileHandler

#from .utils import config as c
#from .utils import futils


class AbbreviatedLoggerNameFormatter(logging.Formatter):
    """Abbreviates logger name to show only first name of each package \
        and full name of the last one.
    """

    def format(self, record):
        # Split the logger name by dots, abbreviate each part except the last
        parts = record.name.split('.')
        if len(parts) > 1:
            record.name = '.'.join(part[0] for part in parts[:-1]) + '.' + parts[-1]
        return super().format(record)


_LOGGER_NAME = 'rterminal'
_LOG_FILENAME = f'{_LOGGER_NAME}.log'
_FORMATTER = AbbreviatedLoggerNameFormatter(
    '{asctime} {name:<25.25} {levelname:<5} {message}',
    style='{'
)

# Log levels
# TODO Load from app config
log_level_console = logging.DEBUG
log_level_file = logging.DEBUG

logger = logging.getLogger(_LOGGER_NAME)
logger.setLevel(logging.DEBUG) # <-- Is it really needed?


# Console handler setup
_ch = logging.StreamHandler()
_ch.setLevel(log_level_console)
_ch.setFormatter(_FORMATTER)
logger.addHandler(_ch)


# TODO: Activate only if config flag is enabled
# Rotating file handler setup
# futils.ensure_dir_existence(cfg.logs_path())
# _fh = RotatingFileHandler(
#     os.path.join(cfg.logs_path(), _LOG_FILENAME),
#     maxBytes=1024 * 1024 * 50,
#     backupCount=5,
#     encoding='utf-8'
# )
# _fh.setLevel(logging.DEBUG)
# _fh.setFormatter(_FORMATTER)
# logger.addHandler(_fh)
