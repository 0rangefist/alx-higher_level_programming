#!/usr/bin/python3

"""
Unittest for Rectangle class
"""
import unittest
from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):
    """
    Unit tests for the Rectangle class
    """
    def setUp(self):
        self.rect1 = Rectangle(2, 10)
        self.rect2 = Rectangle(10, 2, 1, 1, 12)
        self.rect3 = Rectangle(12, 3)

    def test_ids(self):

        self.assertNotEqual(self.rect1.id, self.rect3.id)
        self.assertEqual(self.rect2.id, 12)

    def test_getters(self):
        self.assertEqual(self.rect1.width, 2)
        self.assertEqual(self.rect1.height, 10)
        self.assertEqual(self.rect1.x, 0)
        self.assertEqual(self.rect1.y, 0)

        self.assertEqual(self.rect2.width, 10)
        self.assertEqual(self.rect2.height, 2)
        self.assertEqual(self.rect2.x, 1)
        self.assertEqual(self.rect2.y, 1)

    def test_setters(self):
        self.rect2.width = 5
        self.rect2.height = 9
        self.rect2.x = 2
        self.rect2.y = 3
        self.assertEqual(self.rect2.width, 5)
        self.assertEqual(self.rect2.height, 9)
        self.assertEqual(self.rect2.x, 2)
        self.assertEqual(self.rect2.y, 3)
