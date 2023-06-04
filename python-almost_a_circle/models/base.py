#!/usr/bin/python3
"""
This module contains the Base class
This class will be the base of all other classes in the project.
The goal of it is to manage id attribute in all your future classes
"""


class Base:
    """
    Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor for Base class

        Parameters:
        id (int): id of the Base object, defaults to None
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
