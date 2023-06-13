#!/usr/bin/python3
"""
Thi module defines read_file function
"""


def read_file(filename=""):
    """
    Reads a file and prints the content
    """

    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
