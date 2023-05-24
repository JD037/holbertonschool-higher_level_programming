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
    for i, char in enumerate(text):
        if char in special_chars:
            new_text += char + "\n\n"
        else:
            if i == 0 or text[i-1] not in special_chars:
                new_text += char
    print(new_text, end="")
