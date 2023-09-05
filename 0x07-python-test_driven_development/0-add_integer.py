#!/usr/bin/python3

"""Program for adding two numbers"""


def add_integer(a, b=98):
    """
    Add two integers. If either is float, cast it to integer
    :arg a: an integer or float
    :arg b: an integer or float
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
