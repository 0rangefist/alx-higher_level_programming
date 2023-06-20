#!/usr/bin/python3

"""
Unittest for Base class
"""
import unittest
import os
import json
from unittest.mock import patch
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

    def test_base_from_json_string(self):
        # Test with empty string
        result = Base.from_json_string("")
        self.assertEqual(result, [])

        # Test with string containing empty list
        result = Base.from_json_string("[]")
        self.assertEqual(result, [])

        # Test with None
        result = Base.from_json_string(None)
        self.assertEqual(result, [])

        # Test with valid json string
        json_str = json.dumps([
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ])
        result = Base.from_json_string(json_str)
        expected = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        self.assertEqual(result, expected)

        # Test with no args
        with self.assertRaises(TypeError):
            Base.from_json_string()

        # Test with more than one arg
        with self.assertRaises(TypeError):
            Base.from_json_string("[]", 1)

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

    def test_base_create_rectangle(self):
        # Create a rectangle from a dictionary representation
        dictionary = {'id': 14, 'width': 4, 'height': 2}
        rect = Rectangle.create(**dictionary)
        self.assertEqual(rect.id, 14)
        self.assertEqual(rect.width, 4)
        self.assertEqual(rect.height, 2)

    def test_base_create_square(self):
        # Create a square from a dictionary representation
        dictionary = {'id': 12, 'size': 5}
        square = Square.create(**dictionary)
        self.assertEqual(square.id, 12)
        self.assertEqual(square.size, 5)

    def test_base_create_with_empty_dictionary(self):
        # Instance creation from empty dictionary returns None
        dictionary = {}
        instance = Base.create(**dictionary)
        self.assertIsNone(instance)

    def test_base_create_with_no_args(self):
        # Instance creation with no argument returns None
        instance = Base.create()
        self.assertIsNone(instance)

    def test_base_create_with_excess_args(self):
        # Instance creation with excess arguments should raise TypeError
        dictionary = {'id': 30, 'width': 3, 'height': 8}
        with self.assertRaises(TypeError):
            Rectangle.create("extra_arg", **dictionary)

    def test_base_load_from_file_when_no_file(self):
        # When the file (Rectangle.json) doesn't exist
        rect_list = Rectangle.load_from_file()
        self.assertEqual(rect_list, [])

        # When the file (Square.json) doesn't exist
        rect_list = Square.load_from_file()
        self.assertEqual(rect_list, [])

    def test_base_load_from_file(self):
        # Test for loading rectangles
        rect_list = [Rectangle(4, 5, 0, 0, 15), Rectangle(5, 6, 0, 0, 16)]
        # Save list of rectangles to file
        Rectangle.save_to_file(rect_list)
        # Load list of rectangles from file
        loaded_rect_list = Rectangle.load_from_file()
        # Verify loaded rectangle list
        self.assertEqual(len(loaded_rect_list), 2)
        for elem in loaded_rect_list:
            self.assertTrue(type(elem) == Rectangle)
        self.assertEqual(loaded_rect_list[0].id, 15)
        self.assertEqual(loaded_rect_list[0].width, 4)
        self.assertEqual(loaded_rect_list[0].height, 5)
        self.assertEqual(loaded_rect_list[0].x, 0)
        self.assertEqual(loaded_rect_list[0].y, 0)
        self.assertEqual(loaded_rect_list[1].id, 16)
        self.assertEqual(loaded_rect_list[1].width, 5)
        self.assertEqual(loaded_rect_list[1].height, 6)
        self.assertEqual(loaded_rect_list[1].x, 0)
        self.assertEqual(loaded_rect_list[1].y, 0)

        # Test for loading squares
        square_list = [Square(8, 0, 0, 10), Square(9, 0, 0, 11)]
        # Save list of squares to file
        Square.save_to_file(square_list)
        # Load list of squares from file
        loaded_square_list = Square.load_from_file()
        # Verify loaded square list
        self.assertEqual(len(loaded_square_list), 2)
        for elem in loaded_square_list:
            self.assertTrue(type(elem) == Square)
        self.assertEqual(loaded_square_list[0].id, 10)
        self.assertEqual(loaded_square_list[0].size, 8)
        self.assertEqual(loaded_square_list[0].x, 0)
        self.assertEqual(loaded_square_list[0].y, 0)
        self.assertEqual(loaded_square_list[1].id, 11)
        self.assertEqual(loaded_square_list[1].size, 9)
        self.assertEqual(loaded_square_list[1].x, 0)
        self.assertEqual(loaded_square_list[1].y, 0)

    def test_base_load_from_file_excess_args(self):
        with self.assertRaises(TypeError):
            Base.load_from_file(1)

    def test_base_save_to_file_csv_with_rectangles(self):
        # Create a list of rectangle instances
        rect_list = [Rectangle(10, 5), Rectangle(8, 4)]
        # Save the list of rectangles to a CSV file
        Rectangle.save_to_file_csv(rect_list)
        # Verify that the CSV file exists
        self.assertTrue(os.path.exists("Rectangle.csv"))
        # Verify that the CSV file isn't empty
        if os.path.exists("Rectangle.csv"):
            with open("Rectangle.csv") as file:
                csv_content = file.read()
                self.assertNotEqual(csv_content, "")

    def test_base_save_to_file_csv_with_squares(self):
        # Create a list of square instances
        square_list = [Square(8), Square(9)]
        # Save the list of squares to a CSV file
        Square.save_to_file_csv(square_list)
        # Verify that the CSV file exists
        self.assertTrue(os.path.exists("Square.csv"))
        # Verify that the CSV file isn't empty
        if os.path.exists("Rectangle.csv"):
            with open("Rectangle.csv") as file:
                csv_content = file.read()
                self.assertNotEqual(csv_content, "")

    def test_base_save_to_file_csv_with_empty_list(self):
        # Save an empty list to a CSV file
        Rectangle.save_to_file_csv([])
        # Verify that the CSV file exists
        self.assertTrue(os.path.exists("Rectangle.csv"))
        # Verify that the CSV file is empty
        if os.path.exists("Rectangle.csv"):
            with open("Rectangle.csv") as file:
                csv_content = file.read()
                self.assertEqual(csv_content, "")

    def test_base_save_to_file_csv_with_none_list(self):
        with self.assertRaises(TypeError):
            # Save a None list to a CSV file
            Square.save_to_file_csv(None)

    def test_base_base_load_from_file_csv_with_rectangles(self):
        # Create a list of rectangle instances
        rect_list = [Rectangle(10, 5, 0, 0, 10), Rectangle(8, 4, 0, 0, 11)]
        # Save the list of rectangles to a CSV file
        Rectangle.save_to_file_csv(rect_list)
        # Load the list of rectangles from the CSV file
        loaded_rect_list = Rectangle.load_from_file_csv()
        # Verify the loaded rectangle list
        self.assertEqual(len(loaded_rect_list), 2)
        self.assertEqual(loaded_rect_list[0].id, rect_list[0].id)
        self.assertEqual(loaded_rect_list[0].width, rect_list[0].width)
        self.assertEqual(loaded_rect_list[0].height, rect_list[0].height)
        self.assertEqual(loaded_rect_list[0].x, rect_list[0].x)
        self.assertEqual(loaded_rect_list[0].y, rect_list[0].y)
        self.assertEqual(loaded_rect_list[1].id, rect_list[1].id)
        self.assertEqual(loaded_rect_list[1].width, rect_list[1].width)
        self.assertEqual(loaded_rect_list[1].height, rect_list[1].height)
        self.assertEqual(loaded_rect_list[1].x, rect_list[1].x)
        self.assertEqual(loaded_rect_list[1].y, rect_list[1].y)

    def test_base_load_from_file_csv_with_squares(self):
        # Create a list of square instances
        square_list = [Square(8, 0, 0, 5), Square(9, 0, 0, 6)]
        # Save the list of squares to a CSV file
        Square.save_to_file_csv(square_list)
        # Load the list of squares from the CSV file
        loaded_square_list = Square.load_from_file_csv()
        # Verify the loaded square list
        self.assertEqual(len(loaded_square_list), 2)
        self.assertEqual(loaded_square_list[0].id, square_list[0].id)
        self.assertEqual(loaded_square_list[0].size, square_list[0].size)
        self.assertEqual(loaded_square_list[0].x, square_list[0].x)
        self.assertEqual(loaded_square_list[0].y, square_list[0].y)
        self.assertEqual(loaded_square_list[1].id, square_list[1].id)
        self.assertEqual(loaded_square_list[1].size, square_list[1].size)
        self.assertEqual(loaded_square_list[1].x, square_list[1].x)
        self.assertEqual(loaded_square_list[1].y, square_list[1].y)

    def test_base_load_from_file_csv_with_empty_list(self):
        # Save an empty list of rectangles to a CSV file
        Rectangle.save_to_file_csv([])
        # Load the list of rectangles from the CSV file
        loaded_rect_list = Rectangle.load_from_file_csv()
        # Verify the loaded rectangle list
        self.assertEqual(len(loaded_rect_list), 0)

    def test_base_load_from_file_csv_with_none_list(self):
        with self.assertRaises(TypeError):
            # Save a None list to a CSV file
            Square.save_to_file_csv(None)

    def test_base_load_from_file_csv_with_excess_args(self):
        with self.assertRaises(TypeError):
            # Save to csv with illegal excess arg
            Square.save_to_file_csv([], "excess_arg")

    def tearDown(self):
        # Delete created json files after each test
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        if os.path.exists("Square.json"):
            os.remove("Square.json")

        # Delete created csv files after each test
        if os.path.exists("Rectangle.csv"):
            os.remove("Rectangle.csv")
        if os.path.exists("Square.csv"):
            os.remove("Square.csv")
