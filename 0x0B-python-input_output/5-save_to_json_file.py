#!/usr/bin/python3
"""
Write a function that writes an Object to a text
file, using a JSON representation:

Prototype: def save_to_json_file(my_obj, filename):
You must use the with statement
You don’t need to manage exceptions if the object can’t be serialized.
You don’t need to manage file permission exceptions.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    writes an Object to a text file, using a JSON representation
    """
    with open(filename, encoding="utf-8", mode="w") as f:
        f.write(json.dumps(my_obj))
