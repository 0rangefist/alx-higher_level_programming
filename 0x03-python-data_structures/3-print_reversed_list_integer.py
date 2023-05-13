#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    # handle when input is empty [] or None
    if not my_list:
        return
    for elem in reversed(my_list):
        print("{:d}".format(elem))
