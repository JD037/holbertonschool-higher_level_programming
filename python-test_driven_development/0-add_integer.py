#!/usr/bin/python3
"""
This module contains a function that adds two integers.
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

    if isinstance(a, float):
        if a != a or a == float('inf') or a == -float('inf'):
            raise TypeError("a must be an integer")
        else:
            a = int(a)

    if isinstance(b, float):
        if b != b or b == float('inf') or b == -float('inf'):
            raise TypeError("b must be an integer")
        else:
            b = int(b)

    return a + b
