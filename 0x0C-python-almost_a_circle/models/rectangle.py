#!/usr/bin/python3
"""
This module defines Rectangle class that inherits from Base
"""
from models.base import Base


class Rectangle(Base):
    """
    A Rectangle class
    """
    __nb_objects = 0

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """
        Calculates & returns the area of a Rectangle instance
        """
        return self.width * self.height

    def display(self):
        """
        Prints to stdout the Rectangle instance with # chars
        """
        for row in range(self.y):
            print()
        for row in range(self.height):
            for space in range(self.x):
                print(" ", end="")
            for elem in range(self.width):
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """
        Assigns each element in a list of arguments
        to respective attributes in the Rectangle instance
        1st argument is the id attribute
        2nd argument is the width attribute
        3rd argument is the height attribute
        4th argument is the x attribute
        5th argument is the y attribute
        If *args is empty, each key in **kwargs represents an
        attribute to the instance
        """
        if args and len(args) > 0:
            attrs = ["id", "width", "height", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                # update existing attr that matches the key
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns the dictionary representation of a Rectangle
        """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        return (
            f"[Rectangle] ({self.id}) {self.x}/{self.y} - "
            f"{self.width}/{self.height}"
        )

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
