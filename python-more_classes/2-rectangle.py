#!/usr/bin/python3
"""
This is the "2-rectangle" module.

The 2-rectangle module defines the Rectangle class that has width and height,
and calculates the area and perimeter.
"""


class Rectangle:
    """
    This is the Rectangle class.

    It defines a Rectangle based on width and height, and can calculate
    the rectangle's area and perimeter.
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

    def area(self):
        """Calculate the area of the Rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculate the perimeter of the Rectangle."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)
