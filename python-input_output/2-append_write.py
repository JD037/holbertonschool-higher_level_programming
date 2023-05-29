#!/usr/bin/python3
"""
Module: `2-append_write.py`
"""


def append_write(filename="", text=""):
    """
    Function that appends a string at the end of a UTF8 text file and returns
    the number of characters added.

    Args:
        filename (str): Name of the file to append to.
        text (str): The text to append to the file.

    Returns:
        int: Number of characters added.
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
