#!/usr/bin/env python3
"""Async routine called wait_n that takes
int argument in this order n and max_delay
"""

import asyncio
from random import uniform
from typing import List

async def wait_random(max_delay: int) -> float:
    return uniform(0, max_delay)

async def wait_n(n: int, max_delay: int) -> List[float]:
    delays = [wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*delays)
    return sorted(results)
