#!/usr/bin/python3
"""
This module defines a class BaseGeometry based on `6-base_geometry.py`.
"""


class BaseGeometry:
    """
    Class BaseGeometry with public instance methods area and integer_validator.
    """

    def area(self):
        """
        This method raises an Exception
        with the message "area() is not implemented".
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        This method validates that 'value' is a positive integer.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
