#!/usr/bin/env python3
"""
a type-annotated function make_multiplier that takes
a float multiplier as argument and returns a function
that multiplies a float by multiplier
"""
from typing import Callable
"""
    typing import to get a callable type annotation
"""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    This function takes a float multiplier as argument and
    returns a function that multiplies a float by multiplier
    """
    def func_multiplier(value: float) -> float:
        return value * multiplier

    return func_multiplier
