#!/usr/bin/python3

"""
Unittest for Rectangle class
"""
import unittest
from unittest.mock import patch
from io import StringIO
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
        self.assertNotEqual(self.rect1.id, self.rect2.id)
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

    def test_width_type_validation(self):
        bad_input_types = [None, True, False, 5.5, [1, 2, 3], {"a": 1, "b": 2}]
        for bad_input_type in bad_input_types:
            with self.assertRaisesRegex(TypeError,
                                        "width must be an integer"):
                self.rect1.width = bad_input_type

    def test_width_value_validation(self):
        bad_input_values = [0, -1, -100, -100000]  # 0 and negatives
        for bad_input_value in bad_input_values:
            with self.assertRaisesRegex(ValueError, "width must be > 0"):
                self.rect1.width = bad_input_value

    def test_height_type_validation(self):
        bad_input_types = [None, True, False, 5.5, [1, 2, 3], {"a": 1, "b": 2}]
        for bad_input_type in bad_input_types:
            with self.assertRaisesRegex(TypeError,
                                        "height must be an integer"):
                self.rect1.height = bad_input_type

    def test_height_value_validation(self):
        bad_input_values = [0, -1, -100, -100000]  # 0 and negatives
        for bad_input_value in bad_input_values:
            with self.assertRaisesRegex(ValueError, "height must be > 0"):
                self.rect1.height = bad_input_value

    def test_x_value_validation(self):
        bad_input_values = [-1, -100, -100000]  # negatives
        for bad_input_value in bad_input_values:
            with self.assertRaisesRegex(ValueError, "x must be >= 0"):
                self.rect1.x = bad_input_value

    def test_y_value_validation(self):
        bad_input_values = [-1, -100, -100000]  # negatives
        for bad_input_value in bad_input_values:
            with self.assertRaisesRegex(ValueError, "y must be >= 0"):
                self.rect1.y = bad_input_value

    def test_area(self):
        self.assertEqual(self.rect1.area(), 20)
        # rect2 isn't tested since it may be modified by test_setters()
        self.assertEqual(self.rect3.area(), 36)

    def test_display(self):
        self.rect4 = Rectangle(2, 3)
        expected_output = "##\n##\n##\n"
        with patch("sys.stdout", new=StringIO()) as mock_output:
            self.rect4.display()
            self.assertEqual(mock_output.getvalue(), expected_output)

        self.rect5 = Rectangle(1, 1)
        expected_output = "#\n"
        with patch("sys.stdout", new=StringIO()) as mock_output:
            self.rect5.display()
            self.assertEqual(mock_output.getvalue(), expected_output)

        self.rect6 = Rectangle(2, 3, 1, 2)
        expected_output = "\n\n ##\n ##\n ##\n"
        with patch("sys.stdout", new=StringIO()) as mock_output:
            self.rect6.display()
            self.assertEqual(mock_output.getvalue(), expected_output)

    def test_str(self):
        rect = Rectangle(2, 4, 1, 3, 15)
        rect_str = str(rect)
        self.assertEqual(rect_str, "[Rectangle] (15) 1/3 - 2/4")

    def test_update_with_args(self):
        rect = Rectangle(2, 3, 1, 1, 10)
        rect.update(20, 5, 6, 2, 8)
        self.assertEqual(rect.id, 20)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 6)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 8)

    def test_update_with_kwargs(self):
        rect = Rectangle(3, 6, 2, 4, 22)
        rect.update(height=8, y=7, width=4, x=3)
        self.assertEqual(rect.id, 22)
        self.assertEqual(rect.width, 4)
        self.assertEqual(rect.height, 8)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 7)

    def test_update_with_args_and_kwargs(self):
        rect = Rectangle(12, 16, 1, 9, 23)
        rect.update(25, 4, 8, y=7, x=3)
        self.assertEqual(rect.id, 25)
        self.assertEqual(rect.width, 4)
        self.assertEqual(rect.height, 8)
        self.assertEqual(rect.x, 1)
        self.assertEqual(rect.y, 9)
