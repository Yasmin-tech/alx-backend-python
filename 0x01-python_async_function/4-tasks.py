#!/usr/bin/env python3
''' Implement the coroutine wait_n that calls wait_random
    n times concurrently
    '''


import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    ''' spawn wait_random n times with the specified max_dela
        '''

    tasks = asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    await tasks
    return sorted(tasks.result())
