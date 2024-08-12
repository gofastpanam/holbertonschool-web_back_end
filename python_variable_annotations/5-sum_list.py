#!/usr/bin/env python3
"""
a type-annotated function sum_list which takes
a list input_list of floats as argument
and returns their sum as a float
"""
from typing import List
"""
    typing import to get a list type annotation
"""


def sum_list(input_list: list[float]) -> float:
    """
    Returns sum of a list of floats as a float
    """
    return sum(input_list)
