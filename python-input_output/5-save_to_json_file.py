#!/usr/bin/python3
"""Module for save_to_json_file method."""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file, using a JSON representation.

    Args:
        my_obj: The object to be written.
        filename: The name of the file to write the object to.

    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
