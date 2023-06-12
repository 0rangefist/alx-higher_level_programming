#!/usr/bin/python3

"""
This module defines the class BaseGeometry
"""


class BaseGeometry:
    """
    A Base Geometry class
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
