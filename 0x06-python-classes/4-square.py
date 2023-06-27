#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
A module that defines a Square class with private instance attribute size,
and public instance methods to get and set size,
and calculate the area of the square.

Classes:
    Square

Methods:
    __init__(self, size=0): Initializes an instance of the Square class.
    area(self): Calculates and returns the current square area.
    size(self): Retrieves the value of private instance attribute __size.
    size(self, value): Sets the value of private instance attribute __size.

Raises:
    TypeError: If size is not an integer.
    ValueError: If size is less than or equal to 0.
"""


class Square:
    """
    A class Square that defines a square by: (based on 3-square.py)
        Private instance attribute: size:
            property def size(self): to retrieve it
            property setter def size(self, value): to set it
                size must be an integer, otherwise raise a TypeError exception
                    with the message 'size must be an integer'
                if size is less than 0, raise a ValueError exception
                    with the message 'size must be >= 0'
        Instantiation with optional size: def __init__(self, size=0):
        Public instance method: def area(self):
            that returns the current square area

    Attributes:
        __size (int): The size of a side of the square.

    Methods:
        __init__(self, size=0): Initializes an instance of the Square class.
        area(self): Calculates and returns the current square area.
        size(self): Retrieves the value of private instance attribute __size.
        size(self, value): Sets the value of private instance attribute __size.

    Raises:
        TypeError: If 'value' is not an integer.
        ValueError: If 'value' is less than or equal to 0.
    """

    def __init__(self, size=0):
        """Initializes an instance of the Square class."""

        self.__size = size

    def area(self):
        """Calculates and returns the current square area."""

        return self.__size ** 2

    @property
    def size(self):
        """Retrieves the value of private instance attribute __size."""

        return self.__size

    @size.setter
    def size(self, value):
        """Sets the value of private instance attribute __size."""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
