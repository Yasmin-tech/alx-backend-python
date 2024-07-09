#!/usr/bin/env python3
''' Implement the coroutine measure_time that
    measures the total execution time for wait_n(n, max_delay)
    '''


import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    ''' measures the total execution time for wait_n(n, max_delay),
        and returns total_time / n
        '''

    start = time.perf_counter()
    task = asyncio.run(wait_n(n, max_delay))
    total = time.perf_counter() - start
    # print(task)
    return total / n
