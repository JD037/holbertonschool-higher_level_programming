#!/usr/bin/python3
"""
Module: `0-read_file.py`
"""


def read_file(filename=""):
    """
    Function that reads a UTF8 text file and prints it to stdout.

    Args:
        filename (str): Name of the file to read.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end="")
