#!/usr/bin/python3

"""
This module defines the function inherits_from
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class
    that inherited (directly or indirectly) from the
    specified class otherwise returns False
    """

    if issubclass(type(obj), a_class):
        if a_class != type(obj):
            return True
    return False
