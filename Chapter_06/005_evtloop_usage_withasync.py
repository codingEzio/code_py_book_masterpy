
import time
import asyncio

t = time.time()


async def printer(name):
    print(f"Started {name} at {time.time() - t:.1f}")
    await asyncio.sleep(0.2)
    print(f"Finished {name} at {time.time() - t:.1f}")

# TODO Explaination needed


loop = asyncio.get_event_loop()

result = loop.call_at(
    loop.time() + .2, loop.create_task, printer('call_at'))

result = loop.call_later(.1, loop.create_task, printer('call_later'))
result = loop.call_soon(loop.create_task, printer('call_soon'))

result = loop.call_soon_threadsafe(
    loop.create_task, printer('call_soon_threadsafe'))

result = loop.call_later(1, loop.stop)

loop.run_forever()
