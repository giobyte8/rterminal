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

import backoff


calls_count = 0

class IPv4Error(Exception):
    pass

@backoff.on_exception(
    backoff.expo,
    IPv4Error,
    max_tries=3
)
async def get_ipv4() -> str:
    global calls_count
    calls_count = calls_count + 1

    if calls_count < 2:
        raise IPv4Error()

    return 'lorem'

async def main() -> None:
    print('Alternative service entrypoint')
    print(f'IPv4: { await get_ipv4() }')

if __name__ == '__main__':
    asyncio.run(main())