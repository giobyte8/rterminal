import asyncio
import os
import sys

# If package was not imported from other module
# and package has not been yet installed
if not __package__ and not hasattr(sys, "frozen"):
    rterminal_root = os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
    sys.path.insert(0, os.path.realpath(rterminal_root))

from rterminal.listeners import tg_updates_listener


async def main():
    await tg_updates_listener.start()


if __name__ == '__main__':
    asyncio.run(main())
