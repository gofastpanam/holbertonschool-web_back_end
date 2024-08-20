#!/usr/bin/env python3
"""
this asynchrome function loop 10 times, wait 1 sec
and generate random number between 1 and 10
"""
import asyncio
import random


async def async_generator():
    """
    coroutine that generate random number
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
