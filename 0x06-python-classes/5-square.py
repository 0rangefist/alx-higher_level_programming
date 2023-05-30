#!/usr/bin/python3
"""
This module defines a class Square with a size
"""


class Square:
    """
    Square class with a private size attribute
    """

    def __init__(self, size=0):
        """
        Initialize the Square instance
        """
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculates and returns the current square area
        """
        return self.__size * self.__size

    def my_print(self):
        if self.size == 0:
            print()
            return
        for row in range(self.size):
            for elem in range(self.size):
                print("#", end="")
            print()
