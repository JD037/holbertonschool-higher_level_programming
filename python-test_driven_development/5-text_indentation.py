#!/usr/bin/python3
"""
This is the "5-text_indentation" module.
The 5-text_indentation module supplies one function, text_indentation(text).
"""


def text_indentation(text):
    """Print a text with 2 new lines after each of these characters: ., ? and :
    Args:
        text (str): the text to print
    """
    if type(text) != str:
        raise TypeError('text must be a string')

    special_characters = ['.', '?', ':']
    for char in special_characters:
        text = text.replace(char, char + '\n\n')
    lines = text.split('\n')
    for i, line in enumerate(lines):
        lines[i] = line.strip()
    text = '\n'.join(lines)
    print(text, end="")
