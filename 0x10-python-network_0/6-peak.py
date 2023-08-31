#!/usr/bin/python3
"""This module defines a function that finds a peak in unsorted list"""


def find_peak(list_of_integers):
    """ Find peak in an unsorted list """

    # return None if not list or if empty
    if not list_of_integers:
        return

    # set up the initial left and right index boundaries
    left_index = 0
    right_index = len(list_of_integers) - 1

    # keep the search going until left index == right index
    while left_index != right_index:
        # calculate the middle index
        # this will become the new left or right
        middle_index = int((left_index+right_index)/2)

        # determine where to search, in the left or right half
        # check if the middle value is less than its right neighbour
        if list_of_integers[middle_index] < list_of_integers[middle_index + 1]:
            # we want to search for the peak in the right half
            # so our left_index will now be from middle_index + 1
            # and our right_index remains the same
            left_index = middle_index + 1
        else:  # if middle value is less than left neighbour
            # we want to search for peak in the left half
            # so our right_index will now be middle_index
            # and left_index remains the same
            right_index = middle_index

    # return the number (peak) at the convergent left and right index
    return list_of_integers[right_index]
