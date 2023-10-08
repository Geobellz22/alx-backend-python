#!/usr/bin/env python3
"""Annotated function make_multiplier that takes
multiplier as argument and returns a function
that multiplies a float as multiplier"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a function that multiplies a float
    by the multiplier"""
    def multiplier_function(x: float) -> float:
        return x * multiplier
    return multiplier_function
