#!/usr/bin/python3
"""
This module defines a Base class
"""
import json


class Base:
    """
    A Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:  # assume id is an int
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of a list of dictionaries
        """
        if not list_dictionaries or list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)
