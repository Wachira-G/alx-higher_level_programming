#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest

max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """This class hold the tests for the max_integer function

    Args:
        unittest (module): imports the TestCase class from unittest
    """

    def test_result(self):
        """tests the outputs of various inputs
        """
        self.assertEqual(None, max_integer([]))
        self.assertEqual(4, max_integer([1, 2, 3, 4]))
        self.assertEqual("rer", max_integer(["rer", "hek"]))
        self.assertEqual("r", max_integer("rer"))
        self.assertEqual(6, max_integer([1, 2, 6, 3, 4]))
        self.assertEqual(1, max_integer([1]))

    def test_raises(self):
        """tests if errors are caught, given various inputs
        """
        self.assertRaises(TypeError, max_integer, [1, 2, 3, "hello"])
