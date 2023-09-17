#!/usr/bin/python3

"""
A square class
"""

from .rectangle import Rectangle


class Square(Rectangle):
    """Square class derived from Rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return """[Square] ({:d}) {:d}/{:d} - {:d}""".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Gets the size aka width of self"""
        return self.width

    @size.setter
    def size(self, value):
        """Updates the width and height of self"""
        self.width = value
        self.height = value
