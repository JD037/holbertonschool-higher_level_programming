#!/usr/bin/python3
"""
This module defines a function that prints a square of a given size.

The function raises a TypeError if size is not an integer and a ValueError if
size is less than 0.
"""


def print_square(size):
    """
    Print a square of a given size.

    Args:
        size (int): The size of the square to print.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
