#!/usr/bin/python3
"""
This module defines a Base class
"""
import json
import csv
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

        if cls.__name__ == "Rectangle":
            new_instance = cls(1, 1)  # create dummy instance
        elif cls.__name__ == "Square":
            new_instance = cls(1)  # create dummy instance
        else:
            return None

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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Serializes a list of instaces into a csv file
        """
        filename = cls.__name__ + ".csv"

        # open the csv file for writing
        with open(filename, "w") as file:
            # setup appropriate fieldnames for serialization to csv
            if cls.__name__ == "Rectangle":
                fieldnames = ["id", "width", "height", "x", "y"]
            elif cls.__name__ == "Square":
                fieldnames = ["id", "size", "x", "y"]
            else:
                fieldnames = []

            # we use csv.DictWriter to write a dictionary with
            # specified fieldnames into a csv row
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            # each object's dict repr in the list is saved as a csv row
            for obj in list_objs:
                writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        Deserializes from a csv file back to list of instances
        """
        filename = cls.__name__ + ".csv"

        # if file doesn't exist
        if not os.path.exists(filename):
            return []  # return an empty list

        list_instances = []
        # open the csv file for reading
        with open(filename) as file:
            if cls.__name__ == "Rectangle":
                fieldnames = ["id", "width", "height", "x", "y"]
            elif cls.__name__ == "Square":
                fieldnames = ["id", "size", "x", "y"]
            else:
                fieldnames = []
            # we use csv.DictReader to read each csv row
            # from the file into rows of dictionary objects
            reader = csv.DictReader(file, fieldnames=fieldnames)

            # Iterate over each row in the CSV file
            for row in reader:
                # Convert the values to integers
                for key in row:
                    row[key] = int(row[key])
                # Create an instance from the dictionary
                new_instance = cls.create(**row)
                # Append the instance to the list
                list_instances.append(new_instance)
        return list_instances
