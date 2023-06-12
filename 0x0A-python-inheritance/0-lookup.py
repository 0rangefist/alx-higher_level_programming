#!/usr/bin/python3
"""
This module defines the lookup function
"""


def lookup(obj):
    """
    Returns a list of all available
    attributes & methods of an object
    """
    return dir(obj)
