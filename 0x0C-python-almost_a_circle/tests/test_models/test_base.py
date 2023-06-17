#!/usr/bin/python3

"""
Unittest for Base class
"""
import unittest
from models.base import Base


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
