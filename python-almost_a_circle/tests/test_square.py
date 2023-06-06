#!/usr/bin/env python3
"""Module for TestSquare class"""

import unittest
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


class TestSquare(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_id(self):
        s1 = Square(5)
        self.assertEqual(s1.id, 1)

        s2 = Square(5, 1, 2)
        self.assertEqual(s2.id, 2)

        s3 = Square(5, id=12)
        self.assertEqual(s3.id, 12)

    def test_attributes(self):
        s1 = Square(4, 2, 3, 12)
        self.assertEqual(s1.size, 4)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 3)
        self.assertEqual(s1.id, 12)

    def test_inheritance(self):
        s1 = Square(5)
        self.assertTrue(issubclass(type(s1), Rectangle))
        self.assertTrue(issubclass(type(s1), Base))

    def test_raise(self):
        with self.assertRaises(TypeError):
            s2 = Square()

        with self.assertRaises(ValueError):
            s3 = Square(-3, -3, -3, 12)

        with self.assertRaises(TypeError):
            s4 = Square("hi", [], {}, 12)


if __name__ == "__main__":
    unittest.main()
