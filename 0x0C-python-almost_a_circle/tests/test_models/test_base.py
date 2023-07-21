#!/usr/bin/python3

"""
This module defines unit tests for the Base class.
"""

import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """
    This class represents a collection of unit tests for the Base class.
    """
    @classmethod
    def setUpClass(cls):
        """This method is called once before any tests are run.
        It can be used to set up any expensive resources
        that need to be shared across the test methods.
        """
        cls._Base__nb_objects = 0
        cls.instances = []

    @classmethod
    def tearDownClass(cls):
        """This method is called once after all tests are run.
        It can be used to clean up any resources that were created
        in the setUpClass method.
        """
        cls.instances.clear()

    def setUp(self):
        """
        This method is called b4 each test case to set up the initial state.

        Returns:
        - None
        """
        Base._Base__nb_objects = 0

    def tearDown(self):
        """This method is called after each test method is run.
        It can be used to clean up any resources that were created
        in the setUp method.
        """
        self.instances.clear()

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

    def test_to_json_string(self):
        """tests if the to_json_string method returns the correct output
        """
        self.instances.append(Rectangle(5, 7, 2, 8))
        r1 = self.instances[-1]
        dictionary = r1.to_dictionary()
        json_dict = Base.to_json_string([dictionary])
        self.assertEqual(json_dict,
                         '[{"id": 1, "width": 5, "height": 7, "x": 2, "y": 8}]'
                         )

        self.instances.append(Base())
        blank = self.instances[-1]
        json_str = Base.to_json_string([blank])
        self.assertEqual(json_str, '[]')
        self.assertIsInstance(json_str, str)

    def test_from_json_string(self):
        """Tests if whether the mehtod from_json_string
         deserialises the json string crrectly
        """
        # Test serialisation and deserialisation
        # of a list containing dictionaries
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7},
            ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_output,
                         [{'height': 4, 'width': 10, 'id': 89},
                          {'height': 7, 'width': 1, 'id': 7}])

        # Test None json string returns an empty list
        self.assertEqual(Base.from_json_string(None), [])

        # Test empty json string returns an empty list
        self.assertEqual(Base.from_json_string(''), [])

    def test_create(self):
        """Tests if the create method creates an instance of the class
        """
        self.instances.append(Rectangle(1, 1))
        dummy_instance = self.instances[-1]

        self.instances.append(Rectangle.create(**{'id': 89}))
        r2 = self.instances[-1]
        self.assertNotEqual(dummy_instance, r2)

        self.instances.append(Rectangle.create(**{'id': 89, 'width': 1}))
        r3 = self.instances[-1]
        self.assertNotEqual(dummy_instance, r3)
        self.assertNotEqual(r2, r3)

        self.instances.append(
            Rectangle.create(**{'id': 89, 'width': 1, 'height': 2}))
        r4 = self.instances[-1]
        self.assertNotEqual(dummy_instance, r4)
        self.assertNotEqual(r3, r4)

        self.instances.append(
            Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3}))
        r5 = self.instances[-1]
        self.assertNotEqual(dummy_instance, r5)
        self.assertNotEqual(r4, r5)

        self.instances.append(
            Rectangle.create(
                **{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4}))
        r6 = self.instances[-1]
        self.assertNotEqual(dummy_instance, r6)
        self.assertNotEqual(r5, r6)


if __name__ == "__main__":
    unittest.main()
