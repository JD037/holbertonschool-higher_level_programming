#!/usr/bin/python3
"""
This module defines a class 'Square' that inherits from 'Rectangle'.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A subclass representing a square.
    """

    def __init__(self, size):
        """
        Initialize the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Returns the area of the square.
        """
        return self.__size ** 2
