import os
import logging
from logging.handlers import RotatingFileHandler

import rterminal.utils.config as cfg
from rterminal.utils import futils

_LOGGER_NAME = 'rterminal'
_LOG_FILENAME = f'{_LOGGER_NAME}.log'

logger = logging.getLogger(_LOGGER_NAME)
logger.setLevel(logging.DEBUG)

_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')


## Console handler setup
_ch = logging.StreamHandler()
_ch.setLevel(logging.DEBUG)
_ch.setFormatter(_formatter)
logger.addHandler(_ch)


## Rotating file handler setup
futils.ensure_dir_existence(cfg.logs_path())
_fh = RotatingFileHandler(
    os.path.join(cfg.logs_path(), _LOG_FILENAME),
    maxBytes=1024 * 1024 * 50,
    backupCount=5,
    encoding='utf-8'
)
_fh.setLevel(logging.DEBUG)
_fh.setFormatter(_formatter)
logger.addHandler(_fh)