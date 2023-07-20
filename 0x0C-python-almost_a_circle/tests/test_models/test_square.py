#!/usr/bin/python3

"""
This module defines the unit tests for the Square class
"""

import unittest
from models.square import Square
from models.base import Base


class TestSquare(unittest.TestCase):
    '''
    '''
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

    def test__str__(self):
        '''
        Tests the custom __str__ method
        Update the class Square by overriding the __str__ method
        so that it returns [Square] (<id>) <x>/<y> - <size>

        Returns:
        - None
        '''
        self.instances.append(Square(1))
        rect = self.instances[-1]
        self.assertEqual(rect.__str__(), '[Square] (1) 0/0 - 1')

        self.instances.append(Square(4, 2, 1, 12))
        r1 = self.instances[-1]
        string1 = '[Square] (12) 2/1 - 4'
        self.assertEqual(str(r1), string1)

        self.instances.append(Square(5, 1))
        r2 = self.instances[-1]
        string2 = '[Square] (2) 1/0 - 5'
        self.assertEqual(str(r2), string2)

        self.instances.append(Square(5, 1, 1))
        r3 = self.instances[-1]
        string3 = '[Square] (3) 1/1 - 5'
        self.assertEqual(str(r3), string3)

    def test_size_setter(self):
        """
        Tests if the size is set correctly
        """
        self.instances.append(Square(size=1))
        squa = self.instances[-1]
        self.assertEqual(squa.size, 1)

        with self.assertRaises(TypeError):
            squa.size = '4'
        with self.assertRaises(ValueError):
            squa.size = 0

    def test_update(self):
        """Tests if the update method updates attributes as expected
        """
        self.instances.append(Square(size=1))
        s1 = self.instances[-1]
        s1.update(size=7, id=89, y=1)
        self.assertEqual(s1.size, 7)
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.y, 1)

        s1.update(1, 2, 3, 4)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.size, 2)
        self.assertEqual(s1.x, 3)
        self.assertEqual(s1.y, 4)

        with self.assertRaises(ValueError):
            s1.update(size=-1)

    def test_to_dictionary(self):
        """Tests if the dictionary method
        creates a dictionary of the instance correctly
        """
        self.instances.append(Square(10, 2, 1, 9))
        rect = self.instances[-1]
        self.assertEqual(rect.to_dictionary(),
                         {'size': 10, 'x': 2, 'y': 1, 'id': 9, })

        self.assertListEqual(list(rect.to_dictionary().keys()),
                             ['id', 'size', 'x', 'y', ])


if __name__ == "__main__":
    unittest.main()
