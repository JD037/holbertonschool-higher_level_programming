#!/usr/bin/python3
"""
This module contains a function that checks if an object is an instance of,
or if the object is an instance of a class that inherited from, the specified
class.
"""


def is_kind_of_class(obj, a_class):
    """
    This function checks if obj is an instance of a_class, or if obj is an
    instance of a class that inherited from a_class.

    Parameters:
    obj: Any kind of object.
    a_class: The class to check against.

    Returns:
    True if obj is an instance of a_class, or if obj is an instance of a
    class that inherited from a_class. False otherwise.
    """
    return isinstance(obj, a_class)
