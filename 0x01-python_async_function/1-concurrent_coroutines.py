#!/usr/bin/env python3
"""
Async routine called wait_n that takes in 2 int
arguments (in this order): n and max_delay
"""
import asyncio
from random import uniform
from typing import List

async def wait_random(max_delay: int) -> float:
    """
    Generate a random delay between 0 and max_delay.

    Args:
        max_delay (int): The maximum delay allowed.

    Returns:
        float: A random delay value.

    """
    return uniform(0, max_delay)

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times to generate random delays.

    Args:
        n (int): The number of times to generate random delays.
        max_delay (int): The maximum delay allowed.

    Returns:
        List[float]: A sorted list of random delays.

    """
    delays = [wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*delays)
    return sorted(results)
