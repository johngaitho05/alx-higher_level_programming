#!/usr/bin/python3

"""
Computes the name of a user by concatenating first name and last name
"""


def say_my_name(first_name, last_name=""):
    """
    Compute full name given first name and last name
    :param first_name: the first name of a user
    :param last_name: the last name of a user
    :return: The full name
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
