#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Unit tests for the max_integer function
    """

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_zero_list(self):
        self.assertEqual(max_integer([0, 0, 0, 0, 0, 0]), 0)

    def test_single_num_in_list(self):
        self.assertEqual(max_integer([15]), 15)

    def test_max_at_start_of_list(self):
        self.assertEqual(max_integer([38, 3, 5, 23]), 38)

    def test_max_at_end_of_list(self):
        self.assertEqual(max_integer([0, 3, 5, 23]), 23)

    def test_repeated_max_in_list(self):
        self.assertEqual(max_integer([2, 3, 3, 3, 1]), 3)

    def test_positive_ints_in_list(self):
        self.assertEqual(max_integer([0, 2, 4, 5]), 5)

    def test_negative_ints_in_list(self):
        self.assertEqual(max_integer([-1, -2, -4, -5]), -1)

    def test_mixed_signs_in_list(self):
        self.assertEqual(max_integer([-1, -2, 0, 3, 1]), 3)

    def test_large_list(self):
        nums = list(range(1, 1000001))
        result = max_integer(nums)
        expected = 1000000
        self.assertEqual(result, expected)

    def test_floats_in_list(self):
        self.assertEqual(max_integer([1.5, 2, 0, 3.5, 1]), 3.5)

    def test_strings_in_list(self):
        self.assertEqual(max_integer(["hi", "me", "zoo"]), "zoo")

    def test_non_numbers_in_list(self):
        with self.assertRaises(TypeError):
            max_integer([1, (5, 8)])  # tuple in list
        with self.assertRaises(TypeError):
            max_integer([1, "hello"])  # string in list
        with self.assertRaises(TypeError):
            max_integer([1, None])  # None in list
        with self.assertRaises(TypeError):
            max_integer([1, []])  # list in list

    def test_string_instead_of_list(self):
        self.assertEqual(max_integer("hellozee"), "z")
        self.assertEqual(max_integer("12345699"), "9")

    def test_tuple_instead_of_list(self):
        self.assertEqual(max_integer((1, 8, 70)), 70)
        self.assertEqual(max_integer((-1, -8, -70)), -1)
        self.assertEqual(max_integer((1, 8.5, 3)), 8.5)

    def test_num_instead_of_list(self):
        with self.assertRaises(TypeError):
            max_integer(54)

    def test_set_instead_of_list(self):
        with self.assertRaises(TypeError):
            max_integer({23, 43})

    def test_dict_instead_of_list(self):
        with self.assertRaises(KeyError):
            max_integer({'hi': 34, 'there': 23})
