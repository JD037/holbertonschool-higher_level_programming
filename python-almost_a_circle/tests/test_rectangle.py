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

    def test_rectangle_1(self):
        r = Rectangle(1, 2)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)

    def test_rectangle_2(self):
        r = Rectangle(1, 2, 3)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)

    def test_rectangle_3(self):
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_rectangle_invalid_width_type(self):
        with self.assertRaises(TypeError):
            Rectangle("1", 2)

    def test_rectangle_invalid_height_type(self):
        with self.assertRaises(TypeError):
            Rectangle(1, "2")

    def test_rectangle_invalid_x_type(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")

    def test_rectangle_invalid_y_type(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

    def test_rectangle_invalid_id(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.id, 5)

    def test_rectangle_negative_width(self):
        with self.assertRaises(ValueError):
            r = Rectangle(-1, 2)

if __name__ == "__main__":
    unittest.main()
