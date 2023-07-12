#!/usr/bin/python3

'''A module implementing a simple BaseGeometry class and
A class Rectangle that inherits from BaseGeometry (7-base_geometry.py).
'''

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """a simple class Rectangle inheriting from BaseGeometry
    """

    def __init__(self, width, height):
        """Initializes the class

        Args:
            width (int): the width of the rectangle
            height (int): height of the rectangle
        """
        if self.integer_validator('width', width) is None:
            self.__width = width
        if self.integer_validator('height', height) is None:
            self.__height = height
