#!/usr/bin/env python3
''' Implement the coroutine task_wait_random that takes an integer max_delay
    and returns a asyncio.Task of wait_random
    '''


import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    ''' return the asyncio.task of the coroutine wait_random
        '''

    task = asyncio.create_task(wait_random(max_delay))
    return task
