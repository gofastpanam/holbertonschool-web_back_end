#!/usr/bin/env python3
"""
Annotate function's parameters and return values
with the appropriate types
"""
from typing import Sequence, List, Tuple, Iterable
"""
import module typing
"""


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Args:
        lst: List
    Return: List
    """
    return [(i, len(i)) for i in lst]
