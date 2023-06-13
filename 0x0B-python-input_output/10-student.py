#!/usr/bin/python3

"""
This module defines a Student class
"""


class Student:
    """
    A Student class
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of a Student
        """
        # if attrs is not a list, return the full __dict__
        if type(attrs) != list:
            return self.__dict__

        # else attrs is a list
        for item in attrs:
            # if the list contains non-string elements
            if type(item) != str:  # not a string
                return self.__dict__  # return full __dict__

        # at this point we know we have a list of strings

        # create a new alternate dict
        alt_dict = {}

        # add the  items in attrs that are also
        # present in __dict__ into the new alt_dict
        for item in attrs:
            if item in self.__dict__:
                alt_dict[item] = self.__dict__[item]

        return alt_dict
