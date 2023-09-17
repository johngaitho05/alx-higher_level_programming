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

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Saves objects json representation to a file
        :param list_objs: The objects to save
        """
        dicts = [obj.to_dictionary() for obj in list_objs]
        data = cls.to_json_string(dicts)
        with open(f"{list_objs[0].__class__.__name__}.json",
                  mode='w+', encoding='utf-8') as f:
            f.write(data)


