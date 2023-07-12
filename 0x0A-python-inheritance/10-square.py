#!/usr/bin/python3

'''A module defining a class Square
that inherits from Rectangle (9-rectangle.py)
'''

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """a class Square inheriting rrom the Rectangle class

    Args:
        Rectangle (class): base class defining a rectangle
    """
    def __init__(self, size):
        """initializes an instance of a Square object

        Args:
            size (int): the size of a side of a square
        """
        super().__init__(size, size)
