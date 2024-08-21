#!/usr/bin/env python3
"""
a measure_runtime coroutine that will execute
async_comprehension four times in parallel using asyncio.gather
"""
import asyncio
import time
async_c = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """
    this function measure the total runtime and return it
    """
    start_time = time.perf_counter()
    await asyncio.gather(*(async_c() for i in range(4)))
    end_time = time.perf_counter()
    return end_time - start_time
