#!/usr/bin/python3
"""Add custom attribute to an object"""


def add_attribute(obj, name, value):
    """Add attribute to an object"""
    immutable_types = [int, str, float, tuple,
                       frozenset, bytes, bytearray, bool]

    if obj is None:
        raise TypeError("can't add new attribute")
    for _type in immutable_types:
        if isinstance(obj, _type):
            raise TypeError("can't add new attribute")
    setattr(obj, name, value)
