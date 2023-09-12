#!/usr/bin/python3

"""Reads and prints the content of a file"""


def read_file(filename=""):
    """Read file"""
    with open(filename, 'r') as f:
        print(f.read())
