#!/usr/bin/env python3
''' Implement the coroutine with a Async Generator
    '''


import asyncio
import random
from typing import Generator, AsyncIterable


async def async_generator() -> Generator[float, None, AsyncIterable]:
    ''' Async Generator Coroutine.
        The coroutine will loop 10 times, each time asynchronously,
        wait 1 second, then yield a random number between 0 and 10
        '''
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
