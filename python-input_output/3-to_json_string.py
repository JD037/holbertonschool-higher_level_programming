#!/usr/bin/python3
"""
Module: `3-to_json_string.py`
"""
import json


def to_json_string(my_obj):
    """
    Function that returns the JSON representation of an object (string).

    Args:
        my_obj: The object to convert to a JSON string.

    Returns:
        str: JSON string representation of my_obj.
    """
    return json.dumps(my_obj)
