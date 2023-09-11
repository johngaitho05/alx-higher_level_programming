#!/usr/bin/python3
"""Add custom attribute to an object"""


def add_attribute(obj, name, value):
    """Add attribute to an object"""
    immutable_types = [int, str, float, tuple,
                       frozenset, bytes, bytearray, bool]

    for _type in immutable_types:
        if obj is None or issubclass(obj.__class__, _type):
            raise TypeError("can't add new attribute")
    setattr(obj, name, value)
