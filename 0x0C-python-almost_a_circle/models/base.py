#!/usr/bin/python3
"""
This module defines a Base class
"""
import json
import os


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

    @staticmethod
    def from_json_string(json_string):
        """
        Returns a list (of dictionaries) from a JSON string representation
        """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file
        """
        if list_objs is None:
            list_dictionaries = []
        else:
            list_dictionaries = [obj.to_dictionary() for obj in list_objs]

        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding="utf-8") as file:
            file.write(cls.to_json_string(list_dictionaries))

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set
        """
        if not dictionary:
            return None

        new_instance = cls(1, 1)  # create dummy instance
        new_instance.update(**dictionary)  # dict used as kwargs
        return new_instance

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances
        """
        filename = cls.__name__ + ".json"

        # if file doesn't exist
        if not os.path.exists(filename):
            return []  # return an empty list

        # read json string from a file
        with open(filename) as file:
            json_str = file.read()

        # convert from json string into a list of dictionaries
        dict_list = cls.from_json_string(json_str)

        # convert list of dictionaries into a list of instances
        instance_list = []
        for dict in dict_list:
            # convert each dict into an instance
            new_instance = cls.create(**dict)

            # append the new instance to instance_list
            instance_list.append(new_instance)

        return instance_list
