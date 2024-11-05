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

from rterminal.actions import actions_svc


async def main() -> None:
    await actions_svc.start()
    while True:
        await asyncio.sleep(10)


if __name__ == '__main__':
    asyncio.run(main())
