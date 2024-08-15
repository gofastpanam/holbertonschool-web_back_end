#!/usr/bin/env python3
"""
This function provides an integer argument named wait_random
that waits for a random delay between 0 and max_delay
(included and float value) seconds and eventually returns it.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous function that waits for a random delay and returns the delay.
    """
    number = random.uniform(0, max_delay)
    await asyncio.sleep(number)
    return number
