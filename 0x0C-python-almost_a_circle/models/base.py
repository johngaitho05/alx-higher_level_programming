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

    @staticmethod
    def from_json_string(json_string):
        """
        Retrieves data from a json string
        :param json_string: a json string
        :return: a python object derived from the json string
        """
        return json.loads(json_string) if json_string else ""

    @classmethod
    def create(cls, **dictionary):
        """
        Creates an instance of rectangle or square from a dictionary
        :param dictionary: the kwargs for updating the instance attributes
        :return: the newly created instance
        """
        if 'size' in dictionary:
            obj = cls(size=10)
        else:
            obj = cls(height=5, width=10)
        obj.update(**dictionary)
        return obj



