#!/usr/bin/python3
"""
This module contains a function that adds two integers.
"""

import math


def add_integer(a, b=98):
    """
    Returns the sum of a and b.

    Args:
    a (int, float): The first parameter.
    b (int, float): The second parameter.

    Returns:
    int: The return value. a + b

    Raises:
    TypeError: If a or b are not integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if math.isnan(a):
        raise TypeError("a cannot be NaN")
    if math.isnan(b):
        raise TypeError("b cannot be NaN")

    try:
        a = int(a)
    except OverflowError:
        raise TypeError("a too large to convert to int")
    try:
        b = int(b)
    except OverflowError:
        raise TypeError("b too large to convert to int")

    return a + b
