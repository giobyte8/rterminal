import logging
import os
import sys


# If package was not imported from other module
# and package has not been yet installed
if not __package__ and not hasattr(sys, "frozen"):
    app_root = os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
    sys.path.insert(0, os.path.realpath(app_root))

# Hardcoded import so that '__init__.py' is executed
import rterminal.utils.config as cfg


log = logging.getLogger('rterminal')


if __name__ == "__main__":
    log.info('Running RTerminal')