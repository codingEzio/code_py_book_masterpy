
import asyncio


async def sleepx(delay):
    await asyncio.sleep(delay) 
    print(f'Finished `sleeper` with delay: {delay}') 
    
loop = asyncio.get_event_loop()

result = loop.call_soon(loop.create_task, sleepx(1))
result = loop.call_later(4, loop.stop)

loop.run_forever()