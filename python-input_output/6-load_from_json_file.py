#!/usr/bin/python3
"""Module for load_from_json_file method."""
import json


def load_from_json_file(filename):
    """
    Creates an Object from a JSON file.

    Args:
        filename: The name of the file to load the object from.

    Returns:
        The object loaded from the JSON file.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
