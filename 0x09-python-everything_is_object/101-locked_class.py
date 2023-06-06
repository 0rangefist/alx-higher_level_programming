#!/usr/bin/python3
"""
This module defines the class LockedClass
"""


class LockedClass:
    """
    A LockedClass which prevents any attribute besides first_name
    """
    __slots__ = ("first_name")
