#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Defines test cases for max_integer function
    """

    def test_list_has_items(self):
        """
        test_list_has_items is a method. Calls max_integer with
        an empty list and verifies if None is returned
        """
        self.assertIsNone(max_integer([]))

    def test_returns_max(self):
        """
        test_return_max checks whether the max integer is
        returned given valid inputs
        """
        self.assertEqual(max_integer([2, 7, 9]), 9)

    def test_negative_values(self):
        """
        test the function given negative integers as input
        """
        self.assertEqual(max_integer([-1, 0, -5]), 0)

    def test_same_values(self):
        """
        test the function given similar values
        """
        self.assertEqual(max_integer([1, 1]), 1)

    def test_string_values(self):
        """
        test the function given string values
        """
        self.assertRaises(TypeError, max_integer, [1, "girl", "yes"])

    def test_float_values(self):
        """
        test the function given floating point values
        """
        self.assertEqual(max_integer([1.7, 2.2]), 2.2)

    def test_list(self):
        """
        test the function given a list as input
        """
        self.assertRaises(TypeError, max_integer, [1, [2, 3, 4]])
        self.assertRaises(TypeError, max_integer, ['Hi', 1, 2])

    def test_infinity(self):
        """
        test the function call with infinity
        """
        self.assertEqual(max_integer([100, -100, float('inf')]), float('inf'))
