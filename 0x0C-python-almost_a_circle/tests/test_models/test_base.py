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

    def test_init_without_arg(self):
        # IDs should be unique to every instance
        b1 = Base()
        b2 = Base()
        self.assertNotEqual(b1.id, b2.id)

    def test_init_with_arg(self):
        # ID argument can be used for initialization
        b1 = Base(12)
        self.assertEqual(b1.id, 12)
