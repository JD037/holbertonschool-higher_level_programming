#!/usr/bin/python3
"""
Module: `1-write_file.py`
"""


def write_file(filename="", text=""):
    """
    Function that writes a string to a UTF8 text file and returns
    the number of characters written.

    Args:
        filename (str): Name of the file to write.
        text (str): The text to write in the file.

    Returns:
        int: Number of characters written.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
