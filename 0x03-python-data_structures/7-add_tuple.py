#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # if a tuple has less than 2 elem, replace with (0, 0
    if len(tuple_a) == 0:
        tuple_a = (0, 0)
    if len(tuple_a) == 1:
        tuple_a = (tuple_a[0], 0)

    if len(tuple_b) == 0:
        tuple_b = (0, 0)
    if len(tuple_b) == 1:
        tuple_b = (tuple_b[0], 0)

    # add only the 1st 2 elems of each tuple & return
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
