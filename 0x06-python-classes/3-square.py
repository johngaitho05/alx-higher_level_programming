#!/usr/bin/python3
"""Class Square that defines a square"""


class Square:
    """Class Square that defines a square with attribute size"""

    def __init__(self, size=0):
        """Initializer"""

        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Public instance method that returns te current square area"""
        return self.__size * self.__size
