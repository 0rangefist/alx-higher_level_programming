#!/usr/bin/python3
"""
This module defines the function pascal_triangle
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing
    Pascal's triangle
    """

    # Base cases of n for Pascal's triangle
    if n <= 0:
        return []
    if n == 1:
        return [[1]]
    if n == 2:
        return [[1], [1, 1]]

    # Other cases of n (from n >= 3)
    result_list = [[1], [1, 1]]
    for i in range(3, n+1):
        prev_sub_list = result_list[i-2]
        new_sub_list = []

        for j in range(0, i):
            # first element of new_sub_list
            # is same as first element of prev_sub_list
            if j == 0:
                new_sub_list.append(prev_sub_list[j])

            # last element of new_sub_list
            # is same as lsat element of prev_sub_list
            elif j == i-1:
                new_sub_list.append(prev_sub_list[-1])

            # otherwise new_sublist elem is the sum of prev_sub_list's
            # elem in same position and elem to the left of position
            else:
                new_sub_list.append(prev_sub_list[j] + prev_sub_list[j-1])

        # append the new_sub_list to the result_list
        result_list.append(new_sub_list)
    # return the final result_list
    return result_list
