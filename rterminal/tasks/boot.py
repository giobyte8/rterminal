import logging
import os
import sys

# Add project root to sys.path
if __name__ == '__main__':
    rterm_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    rterm_root = os.path.dirname(rterm_root)
    sys.path.insert(0, os.path.realpath(rterm_root))

from rterminal.clients import central as ctl


log = logging.getLogger(__name__)


if __name__ == "__main__":
    log.info('Executing "boot" task...')
    ctl.notify('RTerminal > Running task: boot')
