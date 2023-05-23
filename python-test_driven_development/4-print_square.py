#!/usr/bin/python3
"""
This is the "4-print_square" module.
The 4-print_square module supplies one function, print_square(size).
"""

def print_square(size):
    """Print a square with the '#' character.
    Args:
        size (int): the size length of the square
    """
    if size is None:
        raise TypeError('missing one argument')
    if type(size) != int:
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')
    else:
        for i in range(size):
            print('#' * size)
