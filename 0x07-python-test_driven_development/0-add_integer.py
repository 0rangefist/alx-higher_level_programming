#!/usr/bin/python3
"""
This module defines add_integer
"""


def add_integer(a, b=98):
    """
    Returns the sum of 2 numbers or if only one argument,
    the sum of the argument and 98
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
