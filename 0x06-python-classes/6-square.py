#!/usr/bin/python3
"""
This module defines a class Square with a size
"""


class Square:
    """
    Square class with a private size attribute
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize the Square instance
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        Calculates and returns the current square area
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Prints a square of #s to stdout using size & position
        """
        if self.size == 0:
            print()
            return
        for row in range(self.position[1]):
            print()
        for row in range(self.size):
            for space in range(self.position[0]):
                print(" ", end="")
            for elem in range(self.size):
                print("#", end="")
            print()
