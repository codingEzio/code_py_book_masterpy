
import asyncio

# adding quotes
#   TODO  thoroughly understood REQUIRED!

"""
The asyncio.Future class is essentially a promise of a result; 
    it returns the results if they are available, 
    
    and once it receives results, 
    it will pass them along to all the registered callbacks. 
    
    It maintains a state variable internally, 
    which allows an outside party to mark a future as canceled. 
"""


async def sleepx(delay):
    await asyncio.sleep(delay)
    print(f'Finished `sleeper` with delay: {delay}')

loop = asyncio.get_event_loop()

# task created
result = loop.call_soon(loop.create_task, sleepx(0.5))

# done after 3 sec
result = loop.call_later(3, loop.stop)

# run forever unless it gets 'loop.stop'
loop.run_forever()
