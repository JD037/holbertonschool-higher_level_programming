#!/usr/bin/python3
"""Module for Square class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes Square instance

        Args:
            size (int): size of the square
            x (int, optional): x position of the square. Defaults to 0.
            y (int, optional): y position of the square. Defaults to 0.
            id (int, optional): id of the square. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Method that returns a string representation
        of the Square instance."""
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.width))
