#!/usr/bin/python3
"""
This module defines load_from_json_file function
"""


def load_from_json_file(filename):

    """
    Creates an Object from a JSON file
    """
    import json

    with open(filename) as f:
        return json.load(f)
