import time
import asyncio

t = time.time()


def printer(name):
    print(f'started {name} at {time.time() - t:.1f}')
    time.sleep(0.2)
    print(f'finished {name} at {time.time() - t:.1f}')

# TODO Explaination needed


loop = asyncio.get_event_loop()

res = loop.call_at(loop.time() + .2, printer, 'call_at')
res = loop.call_later(.1, printer, 'call_later')
res = loop.call_soon(printer, 'call_soon')
res = loop.call_soon_threadsafe(printer, 'call_soon_threadsafe')


# make sure we stop after a sec
res = loop.call_later(1, loop.stop)

loop.run_forever()
