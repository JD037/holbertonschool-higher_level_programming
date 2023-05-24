#!/usr/bin/python3
"""
Module for function text_indentation
"""


def text_indentation(text):
    """
    Function to add two new lines after characters: ., ? and :

    Args:
        text (str): The string to be processed
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
