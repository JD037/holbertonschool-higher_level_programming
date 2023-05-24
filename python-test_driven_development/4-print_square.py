#!/usr/bin/python3
"""
This module contains the print_square function
"""


def print_square(size):
    """
    Function that prints a square with the character #

    Parameters:
    size (int): size length of the square

    Returns:
    None
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
