#!/usr/bin/python3
"""
This module contains a function that checks if an object is an instance
of a specified class.
"""


def is_same_class(obj, a_class):
    """
    This function checks if obj is exactly an instance of a_class.

    Parameters:
    obj: Any kind of object.
    a_class: The class to check against.

    Returns:
    True if obj is exactly an instance of a_class, False otherwise.
    """
    return type(obj) is a_class
