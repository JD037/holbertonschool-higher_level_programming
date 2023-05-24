#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    This class contains unittests for the max_integer() function
    """

    def test_max_integer(self):
        """
        Tests some lists of integers
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([1, 3, -1, 2]), 3)
        self.assertEqual(max_integer([0, 0, 0, 0]), 0)
        self.assertEqual(max_integer([1]), 1)

    def test_empty(self):
        """
        Test an empty list
        """
        self.assertEqual(max_integer([]), None)

    def test_noargs(self):
        """
        Test the function without arguments
        """
        self.assertEqual(max_integer(), None)

    def test_not_list(self):
        """
        Test the function with a non-list argument
        """
        with self.assertRaises(TypeError):
            max_integer("this is not a list")

    def test_list_of_non_ints(self):
        """
        Test the function with a list of non-integers
        """
        with self.assertRaises(TypeError):
            max_integer(["a", "b", "c", "d"])

    def test_list_with_none(self):
        """
        Test the function with a list that contains None
        """
        with self.assertRaises(TypeError):
            max_integer([None])

    def test_list_with_bool(self):
        """
        Test the function with a list that contains a boolean
        """
        self.assertEqual(max_integer([True, False, 2]), 2)
        self.assertEqual(max_integer([True, False]), True)


if __name__ == '__main__':
    unittest.main()
