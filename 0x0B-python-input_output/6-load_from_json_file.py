#!/usr/bin/python3
"""
Write a function that creates an Object from a “JSON file”:

Prototype: def load_from_json_file(filename):
You must use the with statement
You don’t need to manage exceptions if the JSON string
doesn’t represent an object.
You don’t need to manage file permissions / exceptions.
"""

import json


def load_from_json_file(filename):
    """
    Creates an Object from a “JSON file”
    """
    with open(filename, encoding="utf-8", mode="r") as f:
        return json.loads(f.read())
