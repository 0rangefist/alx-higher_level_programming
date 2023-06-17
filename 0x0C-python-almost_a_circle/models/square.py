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

    def __str__(self):
        return (
            f"[Square] ({self.id}) {self.x}/{self.y} - "
            f"{self.width}"
        )
