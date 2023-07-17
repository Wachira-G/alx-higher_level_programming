#!/usr/bin/python3

"""
This module defines unit tests for the Base class.
"""

import unittest
from models.base import Base


class Tests(unittest.TestCase):
    """
    This class represents a collection of unit tests for the Base class.
    """

    def setUp(self):
        """
        This method is called b4 each test case to set up the initial state.

        Returns:
        - None
        """
        Base._Base__nb_objects = 0

    def test_id_assignment(self):
        """
        Tests if the id is correctly assigned when provided or not provided.

        Returns:
        - None
        """

        # id correctly assigned if provided
        instance = Base(12)
        self.assertEqual(instance.id, 12)

        # id correctly assigned if not provided
        instance2 = Base()
        self.assertEqual(instance2.id, 1)  # first instance should have id = 1

    def test_id_uniqueness(self):
        """
        Tests if each instance has a unique id.

        Returns:
        - None
        """

        instance1 = Base()
        instance2 = Base()
        instance3 = Base()
        self.assertNotEqual(instance1.id, instance2.id)
        self.assertNotEqual(instance2.id, instance3.id)
        self.assertNotEqual(instance3.id, instance1.id)

    def test_id_increment(self):
        """
        Tests if the id increments correctly.

        Returns:
        - None
         """

        instance1 = Base()
        instance2 = Base()
        instance3 = Base()
        self.assertEqual(instance1.id, 1)
        self.assertEqual(instance2.id, 2)
        self.assertEqual(instance3.id, 3)


if __name__ == "__main__":
    unittest.main()
