#!/usr/bin/python3

"""
An abstract base class
"""
import json


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializer"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Dumps a list of dicts to a json string
        :param list_dictionaries: a list of python dictionaries
        :return: A JSON string
        """
        return json.dumps(list_dictionaries or [])

