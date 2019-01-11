
import asyncio

# This IS about 'debugging', literally.


async def stack_printer():
    for t in asyncio.Task.all_tasks():
        t.print_stack()

loop = asyncio.get_event_loop()

result = loop.run_until_complete(stack_printer())
