#!/usr/bin/python3
"""
This module contains a function that checks if an object is an instance of a
class that inherited (directly or indirectly) from the specified class.
"""


def inherits_from(obj, a_class):
    """
    This function checks if obj is an instance of a class that inherited
    (directly or indirectly) from a_class.

    Parameters:
    obj: Any kind of object.
    a_class: The class to check against.

    Returns:
    True if obj is an instance of a class that inherited (directly or
    indirectly) from a_class. False otherwise.
    """
    return isinstance(obj, a_class) and type(obj) != a_class
