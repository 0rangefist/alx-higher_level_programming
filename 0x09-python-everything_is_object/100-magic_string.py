#!/usr/bin/python3
def magic_string():
    magic_string.print_count = getattr(magic_string, "print_count", 0) + 1
    return ("BestSchool, " * getattr(magic_string, "print_count", 1))[0:-2]
