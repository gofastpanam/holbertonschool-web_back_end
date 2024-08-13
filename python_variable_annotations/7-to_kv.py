#!/usr/bin/env python3
"""
a type-annotated function to_kv that takes a string k and
an int OR float v as arguments and returns a tuple.
"""
from typing import List, Union
"""
    typing import to get a list type annotation
"""


def to_kv(k: str, v: Union[int, float]) -> tuple:
    """
    this function takes a string k and
    an int OR float v as arguments and returns a tuple
    """
    result: float = v*v 
    return (k, result)
