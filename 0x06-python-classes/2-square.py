#!/usr/bin/python3
"""Square object blueprint"""


class Square:
    """Square object blueprint with attribute size"""

    def __init__(self, size=0):
        """Initializer"""

        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
