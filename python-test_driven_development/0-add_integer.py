#!/usr/bin/python3
"""
This module contains a function that adds two numbers.

The function checks the types of a and b. If they are not integers or floats,
it raises a TypeError. If they are floats, it converts them to integers.
"""


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

    return int(a) + int(b)
