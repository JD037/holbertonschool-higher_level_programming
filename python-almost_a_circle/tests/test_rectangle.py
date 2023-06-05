#!/usr/bin/python3
"""Module for TestRectangle class"""

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for Rectangle class"""

    def test_id(self):
        """Test for id"""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)
        
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 12)

    def test_validation(self):
        """Test for data validation"""
        with self.assertRaises(TypeError):
            r = Rectangle("10", 2)
        with self.assertRaises(ValueError):
            r = Rectangle(-10, 2)
        with self.assertRaises(TypeError):
            r = Rectangle(10, "2")
        with self.assertRaises(ValueError):
            r = Rectangle(10, -2)
        with self.assertRaises(TypeError):
            r = Rectangle(10, 2, "0", 0)
        with self.assertRaises(ValueError):
            r = Rectangle(10, 2, -1, 0)
        with self.assertRaises(TypeError):
            r = Rectangle(10, 2, 0, "0")
        with self.assertRaises(ValueError):
            r = Rectangle(10, 2, 0, -1)


if __name__ == "__main__":
    unittest.main()
