#!/usr/bin/python3

"""Get ready for some calculations"""


class BaseGeometry:
    """I love geometry"""

    def area(self):
        """Too lazy to do this"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Since I'm lazy, I should at least make sure others are not"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
