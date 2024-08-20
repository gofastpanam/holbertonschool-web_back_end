#!/usr/bin/env python3
"""
This async function is a coroutine that
return the 10 random numbers
"""
import asyncio
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """
    This async function is a coroutine that
    return the 10 random numbers
    """
    result = []
    async for i in async_generator():
        result.append(i)
    print(result)
