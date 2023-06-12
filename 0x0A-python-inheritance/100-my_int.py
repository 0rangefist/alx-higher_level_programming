#!/usr/bin/python3
"""
This module implement the class MyInt
"""


class MyInt(int):
    """
    Rebel class MyInt which inverts == and != operators
    """

    def __ne__(self, other):
        return super().__eq__(other)

    def __eq__(self, other):
        return super().__ne__(other)
