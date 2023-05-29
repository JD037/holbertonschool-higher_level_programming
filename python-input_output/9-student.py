#!/usr/bin/python3
"""
This module contains the "Student" class.
"""


class Student:
    """
    A Student class that defines a student by:
        - first_name
        - last_name
        - age
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializer for the Student class.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance.
        """
        return self.__dict__
