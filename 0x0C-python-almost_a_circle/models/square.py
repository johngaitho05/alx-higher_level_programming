#!/usr/bin/python3

"""
A square class
"""

from .rectangle import Rectangle


class Square(Rectangle):
    """Square class derived from Rectangle class"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)