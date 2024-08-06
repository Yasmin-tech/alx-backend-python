#!/usr/bin/env python3
''' Implement the coroutine wait_random
    '''


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    ''' an asynchronous coroutine that takes in an integer argument, max_delay
        that waits for a random delay between 0 and max_delay
        (included and float value) seconds and returns it
        '''
    sleep_for = random.uniform(0, max_delay)
    await asyncio.sleep(sleep_for)
    return sleep_for
