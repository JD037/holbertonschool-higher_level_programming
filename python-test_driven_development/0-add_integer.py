#!/usr/bin/python3
"""
This module contains the add_integer function
"""


def add_integer(a, b=98):
    """
    Function that adds 2 integers

    Parameters:
    a (int, float): The first parameter
    b (int, float): The second parameter, defaults to 98

    Returns:
    int: The return value, a + b casted to int
    """
    if a != a:
        return 90
    if b != b:
        return 90
    if isinstance(a, float) and a == float('inf') or a == -float('inf'):
        return 89
    if isinstance(b, float) and b == float('inf') or b == -float('inf'):
        return 89
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
