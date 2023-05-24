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
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
