#!/usr/bin/python3
"""
This module defines a rectangle class
"""


class Rectangle:
    """
    Base rectangle class
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Returns the area of a rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """
        Returns the perimeter of a rectangle
        """
        if self.width == 0 or self.height == 0:
            return 0
        return (2 * self.width) + (2 * self.height)

    def __str__(self):
        str_output = ""
        if self.width == 0 or self.height == 0:
            return str_output

        # loop over the height
        for i in range(self.height):
            # loop over the width
            for j in range(self.width):
                str_output += str(self.print_symbol)
            if i < self.height - 1:
                str_output += "\n"
        return str_output

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
