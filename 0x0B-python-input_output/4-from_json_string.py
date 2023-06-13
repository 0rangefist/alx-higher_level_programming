#!/usr/bin/python3
"""
This module defines from_json_string function
"""


def from_json_string(my_str):
    """
    Returns an object (Python data structure)
    from a JSON string representation
    """
    import json
    return json.loads(my_str)
