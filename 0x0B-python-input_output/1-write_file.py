#!/usr/bin/python3
"""
This module defines write_file function
"""


def write_file(filename="", text=""):
    """
    Writes to a file & returns number of chars written
    """

    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
