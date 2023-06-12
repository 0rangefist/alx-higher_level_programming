#!/usr/bin/python3
"""
This module defines MyList class
"""


class MyList(list):
    """
    Child class of list that implements print_sorted
    functionality to print ints in a list in ascending order
    """

    def print_sorted(self):
        """
        Prints a list of ints in ascending order
        """
        print(sorted(self))
