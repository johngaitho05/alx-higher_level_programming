#!/usr/bin/python3

"""
Program for adding 2 numbers
"""


def add_integer(a, b=98):

    """
    Function that adds 2 integers. a and b must be integers or floats,
    otherwise TypeError exception is raised with the message
    a must be an integer or b must be an integer. a and b are also
    cast into integer if they are float.
    """

    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
