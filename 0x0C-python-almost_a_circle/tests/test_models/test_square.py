#!/usr/bin/python3

"""
Unittest for Square class
"""
import unittest
from models.square import Square


class TestSquareClass(unittest.TestCase):
    """
    Unit tests for the Square class (which inherits from Rectangle)
    """
    def test_square_init(self):
        # init with only size & default args
        square = Square(5)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 0)
        self.assertIsNotNone(square.id)

        # init with all args
        square = Square(6, 1, 3, 15)
        self.assertEqual(square.width, 6)
        self.assertEqual(square.height, 6)
        self.assertEqual(square.x, 1)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.id, 15)

    def test_square_str(self):
        square = Square(4, 1, 2, 10)
        square_str = str(square)
        self.assertEqual(square_str, "[Square] (10) 1/2 - 4")

    def test_square_size_getter(self):
        square = Square(5)
        self.assertEqual(square.size, 5)

    def test_square_size_setter(self):
        square = Square(5)
        square.size = 8
        self.assertEqual(square.size, 8)
        self.assertEqual(square.width, 8)
        self.assertEqual(square.height, 8)

    def test_square_update_with_args(self):
        square = Square(5, 2, 3, 10)
        square.update(15, 6, 4, 8)
        self.assertEqual(square.id, 15)
        self.assertEqual(square.width, 6)
        self.assertEqual(square.height, 6)
        self.assertEqual(square.size, 6)
        self.assertEqual(square.x, 4)
        self.assertEqual(square.y, 8)

    def test_square_update_with_kwargs(self):
        square = Square(4, 1, 2, 10)
        square.update(x=3, y=4, id=20, size=7)
        self.assertEqual(square.id, 20)
        self.assertEqual(square.width, 7)
        self.assertEqual(square.height, 7)
        self.assertEqual(square.size, 7)
        self.assertEqual(square.x, 3)
        self.assertEqual(square.y, 4)

    def test_square_update_with_args_and_kwargs(self):
        # kwargs will be skipped per the requirements
        square = Square(3, 2, 1, 5)
        square.update(10, 5, x=3, y=2)
        self.assertEqual(square.id, 10)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 1)
