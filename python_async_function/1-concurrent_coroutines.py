#!/usr/bin/env python3
"""
an async routine called wait_n that takes in 2 int arguments
(in this order): n and max_delay
"""
import asyncio
import random
from typing import List

wait_r = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with the specified max_delay.
    Return the list of all the delays in ascending order.
    """
    delays = await asyncio.gather(*(wait_r(max_delay) for i in range(n)))
    sorted_delays = []
    for delay in delays:
        inserted = False
        for i in range(len(sorted_delays)):
            if delay < sorted_delays[i]:
                sorted_delays.insert(i, delay)
                inserted = True
                break
        if not inserted:
            sorted_delays.append(delay)
    return sorted_delays
