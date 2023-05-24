#!/usr/bin/python3
"""Module for text_indentation function"""


def text_indentation(text):
    """Function that indents text after each '.', '?' and ':'.

    Args:
    text (str): The text to indent.

    Raises:
    TypeError: If text is not a string.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    special_chars = ['.', '?', ':']
    new_text = ""
    start = 0
    for i, char in enumerate(text):
        if char in special_chars:
            # trim right spaces before special characters and append
            new_text += text[start:i].rstrip() + char + "\n\n"
            start = i + 1  # update start for next section
    new_text += text[start:].rstrip()  # append last section
    print(new_text, end="")
