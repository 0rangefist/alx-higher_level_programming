#!/usr/bin/python3
"""
This module defines save_to_json_file function
"""


def save_to_json_file(my_obj, filename):

    """
    Writes an Object to a text file,
    using a JSON representation:
    """
    import json

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
