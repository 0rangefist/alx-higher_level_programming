#!/usr/bin/python3
"""
This module defines the function is_same_class
"""


def is_same_class(obj, a_class):
    """
    Returns True if the object is exactly an instance
    of a specified class otherwise returns False
    """

    if type(obj) == a_class:
        return True
    return False
