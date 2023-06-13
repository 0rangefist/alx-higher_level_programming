#!/usr/bin/python3
"""
This module defines append_write function
"""


def append_write(filename="", text=""):
    """
    Writes to a file & returns number of chars written
    """

    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
