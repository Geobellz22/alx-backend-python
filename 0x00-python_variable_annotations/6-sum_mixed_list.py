#!/usr/bin/env python3
"""Type annotated function sum_mixed_list which takes
a list mxd_list of integers and float
abd returns their sum as float"""


from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """Returns sum of float"""
    return sum(mxd_list)
