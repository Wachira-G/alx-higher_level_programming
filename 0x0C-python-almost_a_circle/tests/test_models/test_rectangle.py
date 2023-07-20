#!/usr/bin/python3

"""
This module defines unit tests for the Rectangle class.
"""

import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """
    This class represents a collection of unit tests for the Rectangle class.
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
        """This method is called before each test method is run.
        It can be used to set up any resources that are needed
        by the test methods.
        """
        Base._Base__nb_objects = 0

    def tearDown(self):
        """This method is called after each test method is run.
        It can be used to clean up any resources that were created
        in the setUp method.
        """
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

        self.instances.append(Rectangle(1, 2, 3, 4, 5))
        rec = self.instances[-1]
        self.assertEqual(rec.width, 1)
        self.assertEqual(rec.height, 2)
        self.assertEqual(rec.x, 3)
        self.assertEqual(rec.y, 4)
        self.assertEqual(rec.id, 5)

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

        with self.assertRaises(ValueError):
            Rectangle(-1, 2, 3, 4, None)  # negative width

        with self.assertRaises(ValueError):
            Rectangle(1, -2, 3, 4, None)  # negative height

        with self.assertRaises(TypeError):
            Rectangle("1", 2, 3, 4, None)  # string width

        with self.assertRaises(TypeError):
            Rectangle(1, "2", 3, 4, None)  # string height

        with self.assertRaises(TypeError):
            Rectangle(1.1, 1, 0, 0)  # float width

        with self.assertRaises(TypeError):
            Rectangle(1, 1.2, 0, 0)  # float width

        with self.assertRaises(ValueError):
            Rectangle(1, 1, -1, 0)  # negative x

        with self.assertRaises(ValueError):
            Rectangle(1, 1, 0, -1)  # negative y

        with self.assertRaises(TypeError):
            Rectangle(1, 1, '3')  # string x

        with self.assertRaises(TypeError):
            Rectangle(1, 1, 0, '4')  # string y

        with self.assertRaises(ValueError):
            Rectangle(1, 0)  # zero height

        with self.assertRaises(ValueError):
            Rectangle(0, 1)  # zero width

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

        with self.assertRaises(ValueError):
            rect.width = 0  # width = 0

        with self.assertRaises(ValueError):
            rect.height = 0  # height = 0

        with self.assertRaises(ValueError):
            rect.width = -1  # width < 0

        with self.assertRaises(ValueError):
            rect.height = -2  # height < 0

        with self.assertRaises(TypeError):
            rect.x = "5"  # Invalid x type

        with self.assertRaises(TypeError):
            rect.y = "4"  # Invalid y type

        with self.assertRaises(ValueError):
            rect.x = -1  # x < 0

        with self.assertRaises(ValueError):
            rect.y = -3  # y < 0

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

        self.instances.append(Rectangle(2, 3, 2, 2))
        r2 = self.instances[-1]
        expected_output = '\n\n  ##\n  ##\n  ##\n'

        #  Redirect stdout to capture print output
        import sys
        from io import StringIO

        captured_output = StringIO()
        sys.stdout = captured_output

        r2.display()

        #  Reset stdout
        sys.stdout = sys.__stdout__

        self.assertEqual(captured_output.getvalue(), expected_output)

        self.instances.append(Rectangle(2, 3, 2))
        r3 = self.instances[-1]
        expected_output = '  ##\n  ##\n  ##\n'

        #  Redirect stdout to capture print output
        import sys
        from io import StringIO

        captured_output = StringIO()
        sys.stdout = captured_output

        r3.display()

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
        self.instances.append(Rectangle(1, 2))
        rect = self.instances[-1]
        self.assertEqual(rect.__str__(), '[Rectangle] (1) 0/0 - 1/2')

        self.instances.append(Rectangle(4, 6, 2, 1, 12))
        r1 = self.instances[-1]
        string1 = '[Rectangle] (12) 2/1 - 4/6'
        self.assertEqual(str(r1), string1)

        self.instances.append(Rectangle(5, 5, 1))
        r2 = self.instances[-1]
        string2 = '[Rectangle] (2) 1/0 - 5/5'
        self.assertEqual(str(r2), string2)

    def test_update(self):
        '''Tests correct update to attributes:
        1st argument should be the id attribute
        2nd argument should be the width attribute
        3rd argument should be the height attribute
        4th argument should be the x attribute
        5th argument should be the y attribute

        Returns:
        - None
        '''
        # Create a Rectangle instance
        self.instances.append(Rectangle(5, 5))
        r1 = self.instances[-1]

        # Test update with args of size zero
        r1.update()
        self.assertEqual(r1.id, 1)

        # Test update with args of size one
        r1.update(89)
        self.assertEqual(r1.id, 89)

        # Test update with args of size 2
        r1.update(2, 3)
        self.assertEqual(r1.width, 3)

        # Test update with args of size 3
        r1.update(4, 5, 6)
        self.assertEqual(r1.height, 6)

        # Test update with args of size 4
        r1.update(7, 8, 9, 10)
        self.assertEqual(r1.x, 10)

        # Test update with args of size 5
        r1.update(11, 12, 13, 14, 15)
        self.assertEqual(r1.y, 15)

        # with self.assertRaises(TypeError): # extra args
        #    r1.update(11, 12, 13, 14, 15, 16)

        # KWARGS TESTS
        self.tearDown()
        self.setUp()
        # Create a Rectangle instance
        self.instances.append(Rectangle(10, 10, 10, 10))
        rect = self.instances[-1]
        self.assertEqual(str(rect), "[Rectangle] (1) 10/10 - 10/10")

        # Test update with keyword argument height=1
        rect.update(height=1)
        self.assertEqual(str(rect), "[Rectangle] (1) 10/10 - 10/1")

        # Test update with keyword arguments width=1 and x=2
        rect.update(width=1, x=2)
        self.assertEqual(str(rect), "[Rectangle] (1) 2/10 - 1/1")

        # Test update with keyword arguments y=1, width=2, x=3, id=89
        rect.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(rect), "[Rectangle] (89) 3/1 - 2/1")

        # Test update with keyword arguments x=1, height=2, y=3, width=4
        rect.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(rect), "[Rectangle] (89) 1/3 - 4/2")

        # Test update with keyword arguments x=1, height=2, y=3, width=4, id=98
        rect.update(x=1, height=2, y=3, width=4, id=98)
        self.assertEqual(str(rect), "[Rectangle] (98) 1/3 - 4/2")

        # Test update with both args and kwargs
        rect.update(89, 10, width=11)
        self.assertEqual(str(rect), "[Rectangle] (89) 1/3 - 10/2")

        # Test update with kwargs
        rect.update(**{'id': 98})
        self.assertEqual(rect.id, 98)
        # Test update with kwargs
        rect.update(**{'id': 89, 'width': 2})
        self.assertEqual(rect.width, 2)
        # Test update with kwargs
        rect.update(**{'id': 89, 'width': 1, 'height': 4})
        self.assertEqual(rect.height, 4)
        # Test update with kwargs
        rect.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 9})
        self.assertEqual(rect.x, 9)
        # Test update with kwargs
        rect.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 8})
        self.assertEqual(rect.y, 8)

    def test_to_dictionary(self):
        """Tests if the method to_dictionary converts instance
         to correct dictionary representation
        """
        self.instances.append(Rectangle(10, 2, 1, 9))
        rect = self.instances[-1]
        self.assertEqual(rect.to_dictionary(),
                         {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10})

        self.assertListEqual(list(rect.to_dictionary().keys()),
                             ['id', 'width', 'height', 'x', 'y', ])

        self.instances.append(Rectangle(10, 7, 2, 8))
        r1 = self.instances[-1]
        dictionary = r1.to_dictionary()
        self.assertDictEqual(dictionary,
                             {"x": 2, "width": 10, "id": 2,
                              "height": 7, "y": 8})


if __name__ == "__main__":
    unittest.main()
