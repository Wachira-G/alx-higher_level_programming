#!/usr/bin/python3

"""
This module defines unit tests for the Rectangle class.
"""

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    This class represents a collection of unit tests for the Rectangle class.
    """
    instances = []

    @classmethod
    def setUpClass(cls):
        """This method is called once before any tests are run.
        It can be used to set up any expensive resources
        that need to be shared across the test methods.
        """
        pass

    @classmethod
    def tearDownClass(cls):
        """This method is called once after all tests are run.
        It can be used to clean up any resources that were created
        in the setUpClass method.
        """
        pass

    def setUp(self):
        """This method is called before each test method is run.
        It can be used to set up any resources that are needed
        by the test methods.
        """
        self.instances = []

    def tearDown(self):
        """This method is called after each test method is run.
        It can be used to clean up any resources that were created
        in the setUp method.
        """
        for instance in self.instances:
            del instance
        self.instances.clear()

    def test_initialization(self):
        """
        Tests if the Rectangle object is initialized correctly.

        Returns:
        - None
        """

        self.instances.append(Rectangle(1, 2))
        rect = self.instances[-1]
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 0)
        self.assertIsNotNone(rect.id)

    def test_invalid_inputs(self):
        """
        Tests if the Rectangle object raises exceptions for invalid inputs.

        Returns:
        - None
        """

        with self.assertRaises(TypeError):
            Rectangle()  # no arguments

        with self.assertRaises(TypeError):
            Rectangle(2)  # less arguments

        with self.assertRaises(TypeError):
            Rectangle(-1, 2, 3, 4, None)  # negative width

        with self.assertRaises(TypeError):
            Rectangle(1, -2, 3, 4, None)  # negative height

        with self.assertRaises(TypeError):
            Rectangle("1", 2, 3, 4, None)  # string width

        with self.assertRaises(TypeError):
            Rectangle(1, "2", 3, 4, None)  # string height

        with self.assertRaises(TypeError):
            Rectangle(1.1, 1, 0, 0)  # float width

        with self.assertRaises(TypeError):
            Rectangle(1, 1.2, 0, 0)  # float width

        with self.assertRaises(TypeError):
            Rectangle(1, 1, -1, 0)  # negative x

        with self.assertRaises(TypeError):
            Rectangle(1, 1, 0, -1)  # negative y

    def test_property_setters(self):
        """
        Tests if the property setters of the Rectangle object
          raise exceptions for invalid inputs.

        Returns:
        - None
         """

        self.instances.append(Rectangle(1, 2))
        rect = self.instances[-1]
        with self.assertRaises(TypeError):
            rect.width = "3"  # Invalid width type

        with self.assertRaises(TypeError):
            rect.height = "3"  # Invalid height type

        with self.assertRaises(TypeError):
            rect.width = None  # Invalid width type

        with self.assertRaises(TypeError):
            rect.height = None  # Invalid height type

        with self.assertRaises(TypeError):
            rect.x = "5"  # Invalid x type

        with self.assertRaises(TypeError):
            rect.y = "4"  # Invalid y type

    def test_area(self):
        '''Tests if the area property returns the correct values

        Returns:
        - None
        '''
        self.instances.append(Rectangle(1, 2))
        rect = self.instances[-1]
        self.assertEqual(rect.area(), 2)

        rect.width = 2
        self.assertEqual(rect.area(), 4)

    def test_display(self):
        '''
        Tests if the display method correctly displays the rectangle.

        Returns:
        - None
        '''

        self.instances.append(Rectangle(4, 6))
        r1 = self.instances[-1]
        expected_output = '####\n####\n####\n####\n####\n####\n'

        #  Redirect stdout to capture print output
        import sys
        from io import StringIO

        captured_output = StringIO()
        sys.stdout = captured_output

        r1.display()

        #  Reset stdout
        sys.stdout = sys.__stdout__

        self.assertEqual(captured_output.getvalue(), expected_output)

    def test__str__(self):
        '''
        Tests the custom __str__ method
        Update the class Rectangle by overriding the __str__ method
        so that it returns [Rectangle] (<id>) <x>/<y> - <width>/<height>

        Returns:
        - None
        '''
        rect = Rectangle(1, 2)
        self.assertEqual(rect.__str__(), '[Rectangle] (1) 0/0 - 1/2')

        r1 = Rectangle(4, 6, 2, 1, 12)
        string1 = '[Rectangle] (12) 2/1 - 4/6'
        self.assertEqual(str(r1), string1)

        r2 = Rectangle(5, 5, 1)
        string2 = '[Rectangle] (2) 1/0 - 5/5'
        self.assertEqual(str(r2), string2)


if __name__ == "__main__":
    unittest.main()
