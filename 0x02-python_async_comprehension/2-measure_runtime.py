#!/usr/bin/env python3
''' Import async_comprehension from the previous file
    and implement a measure_runtime coroutine that will execute
    async_comprehension four times in parallel using asyncio.gather
    '''


import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    ''' Async Coroutine that will create a list resulted
        from calling async_generator using list comprehension
        '''
    start = time.time()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    total = time.time() - start

    return total
