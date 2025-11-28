import logging
import os
import sys

# Add project root to sys.path
if __name__ == '__main__':
    rterm_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    rterm_root = os.path.dirname(rterm_root)
    sys.path.insert(0, os.path.realpath(rterm_root))

from rterminal.clients import central as ctl
from rterminal.clients import ipfy


log = logging.getLogger('rterminal')


if __name__ == "__main__":
    log.info('Running task: host_status_update')

    ipv4_public = ipfy.get_public_ip()
    ctl.update_host_status(ipv4_public)