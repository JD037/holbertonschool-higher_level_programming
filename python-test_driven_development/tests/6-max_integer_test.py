#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest


from 6-max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_at_end(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_in_middle(self):
        self.assertEqual(max_integer([1, 4, 3, 2]), 4)

    def test_one_negative(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_all_negative(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_one_element(self):
        self.assertEqual(max_integer([1]), 1)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_not_a_list(self):
        with self.assertRaises(TypeError):
            max_integer("This is not a list")

    def test_list_of_strings(self):
        with self.assertRaises(TypeError):
            max_integer(["This", "is", "a", "list", "of", "strings"])

if __name__ == "__main__":
    unittest.main()
