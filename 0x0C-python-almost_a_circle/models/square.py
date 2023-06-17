#!/usr/bin/python3

"""
This module defines a Square class which inherits from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    A square class
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def update(self, *args, **kwargs):
        """
        Assigns each element in a list of arguments
        to respective attributes in the Rectangle instance
        1st argument is the id attribute
        2nd argument is the size attribute
        3th argument is the x attribute
        4th argument is the y attribute
        If *args is empty, each key in **kwargs represents an
        attribute to the instance
        """
        if args and len(args) > 0:
            attrs = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                # update existing attr that matches the key
                if hasattr(self, key):
                    setattr(self, key, value)

    def __str__(self):
        return (
            f"[Square] ({self.id}) {self.x}/{self.y} - "
            f"{self.width}"
        )

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
