#!/usr/bin/env python3
"""Coroutine that takes in an argument
that takes in an integer argument max_delay
with a default value of 10"""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """wait for a random delay between 0
    and max_delay"""
    delay_time = random.uniform(0, max_delay)
    await asyncio.sleep(delay_time)
    return delay_time
