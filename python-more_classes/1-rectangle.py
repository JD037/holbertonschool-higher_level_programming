#!/usr/bin/python3
"""
This is the "1-rectangle" module.

The 1-rectangle module defines the Rectangle class.
"""


class Rectangle:
    """
    This is the Rectangle class.

    It defines a Rectangle based on width and height.
    """

    def __init__(self, width=0, height=0):
        """
        Initialize the Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width.

        Raise TypeError if value is not an int.
        Raise ValueError if value is < 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height.

        Raise TypeError if value is not an int.
        Raise ValueError if value is < 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
