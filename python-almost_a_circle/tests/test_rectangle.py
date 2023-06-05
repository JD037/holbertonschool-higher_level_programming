#!/usr/bin/python3
"""Module for TestRectangle class"""

import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_id(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(10, 2)
        self.assertEqual(r2.id, 2)
        r3 = Rectangle(10, 2, id=12)
        self.assertEqual(r3.id, 12)

    def test_attributes(self):
        r1 = Rectangle(4, 2, 1, 1, 12)
        self.assertEqual(r1.width, 4)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.y, 1)
        self.assertEqual(r1.id, 12)

    def test_raise(self):
        with self.assertRaises(TypeError):
            r4 = Rectangle()

        with self.assertRaises(ValueError):
            r5 = Rectangle(-3, -3, -1, -1, 12)

        with self.assertRaises(TypeError):
            r6 = Rectangle("hi", "hello", [], {}, 12)


if __name__ == "__main__":
    unittest.main()
