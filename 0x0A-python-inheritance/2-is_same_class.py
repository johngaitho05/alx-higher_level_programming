#!/usr/bin/python3
"""Checks whether an object is an instance of a class"""


def is_same_class(obj, a_class):
    """Check if object is instance of class"""
    return issubclass(a_class, obj.__class__)
