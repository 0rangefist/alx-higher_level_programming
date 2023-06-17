#!/usr/bin/python3

"""
Unittest for Base class
"""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseClass(unittest.TestCase):
    """
    Unit tests for the Base class
    """

    def test_base_init_without_arg(self):
        # IDs should be unique to every instance
        b1 = Base()
        b2 = Base()
        self.assertNotEqual(b1.id, b2.id)

    def test_base_init_with_arg(self):
        # ID argument can be used for initialization
        b1 = Base(12)
        self.assertEqual(b1.id, 12)

    def test_base_to_json_string(self):
        # Test with empty list
        json_str = Base.to_json_string([])
        self.assertEqual(json_str, "[]")

        # Test with None
        json_str = Base.to_json_string(None)
        self.assertEqual(json_str, "[]")

        # Test with list of dictionaries
        dicts = [
            {"id": 1, "size": 5},
            {"id": 2, "size": 3}
        ]
        expected_json_str = '[{"id": 1, "size": 5}, {"id": 2, "size": 3}]'
        json_str = Base.to_json_string(dicts)
        self.assertEqual(json_str, expected_json_str)

        # Test with no args
        with self.assertRaises(TypeError):
            Base.to_json_string()

        # Test with more than one arg
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)

    def test_base_save_to_file_rect(self):
        # Test saving a list of Rectangles to a JSON file
        r1 = Rectangle(10, 7, 2, 8, 20)
        r2 = Rectangle(5, 5, 1, 1, 21)
        Rectangle.save_to_file([r1, r2])

        # Check if the file exists
        self.assertTrue(os.path.exists("Rectangle.json"))

        # Read JSON file and check its contents
        with open("Rectangle.json", "r") as file:
            read_content = file.read()
            expected = ('[{"id": 20, "width": 10, "height": 7, "x": 2, "y": 8}'
                        ', {"id": 21, "width": 5,'
                        ' "height": 5, "x": 1, "y": 1}]')
            self.assertEqual(read_content, expected)

    def test_base_save_to_file_square(self):
        # Test saving a list of Square objects to a file
        s1 = Square(5, 0, 0, 29)
        s2 = Square(8, 2, 4, 30)
        Square.save_to_file([s1, s2])

        # Check if the file exists
        self.assertTrue(os.path.exists("Square.json"))

        # Read the file and check its contents
        with open("Square.json", "r") as file:
            read_content = file.read()
            expected = ('[{"id": 29, "size": 5, "x": 0, "y": 0},'
                        ' {"id": 30, "size": 8, "x": 2, "y": 4}]')
            self.assertEqual(read_content, expected)

    def test_base_save_to_file_empty_list(self):
        # Test saving an empty list to a file
        Rectangle.save_to_file([])
        self.assertTrue(os.path.exists("Rectangle.json"))

        # Read the file and check its contents
        with open("Rectangle.json", "r") as file:
            read_content = file.read()
            self.assertEqual(read_content, "[]")

    def test_base_save_to_file_none(self):
        # Test saving None to a file
        Rectangle.save_to_file(None)
        self.assertTrue(os.path.exists("Rectangle.json"))

        # Read the file and check its contents
        with open("Rectangle.json", "r") as file:
            read_content = file.read()
            self.assertEqual(read_content, "[]")

    def tearDown(self):
        # Delete the created files after each test
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        if os.path.exists("Square.json"):
            os.remove("Square.json")
