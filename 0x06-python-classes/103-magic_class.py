#!/usr/bin/python3
"""
This module implements MagicClass which calculates the area
and circumference of a circle given its raduis
"""


class MagicClass:
    """
    This class creates circle objects
    """
    def __init__(self, radius=0):

        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """
        Calculate the area of a circle from its radius
        """
        from math import pi
        return (self.__radius ** 2) * pi

    def circumference(self):
        """
        Calculate the circumference of a circle from its radius
        """
        from math import pi
        return (2 * pi) * self.__radius
