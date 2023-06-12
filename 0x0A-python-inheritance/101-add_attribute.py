#!/usr/bin/python3
"""
This module defines add_attribute
"""


def add_attribute(obj, attr_name, attr_value):
    """
    Adds a new attribute to an object if possible
    otherwise throws a TypeError exception
    """

    # check if the object doesnt have the __dict__ attribute,
    # ie. if it doesnt support dynamic attribute assignment
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")

    # otherwise set the new attribute as an attribute of object
    setattr(obj, attr_name, attr_value)
