#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
A module that defines a Square class with private instance attribute size,
and public instance methods to get and set size,
calculate the area of the square, and print the square.

Classes:
    Square

Methods:
    __init__(self, size=0): Initializes an instance of the Square class.
    area(self): Calculates and returns the current square area.
    size(self): Retrieves the value of private instance attribute __size.
    size(self, value): Sets the value of private instance attribute __size.
    my_print(self): Prints in stdout a square with '#' character.

Raises:
    TypeError: If 'value' is not an integer.
    ValueError: If 'value' is less than or equal to 0.
"""


class Square:
    """
    A class Square that defines a square by: (based on 4-square.py)
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
        Public instance method: def my_print(self):
            that prints in stdout the square with the character #:
                if size is equal to 0, print an empty line

    Attributes:
        __size (int): The length of one side of a square.

    Methods:
        __init__(self, size=0): Initializes an instance of the Square class.
        area(self): Calculates and returns the current square area.
        size(self): Retrieves the value of private instance attribute __size.
        size(self, value): Sets the value of private instance attribute __size.
        my_print(self): Prints in stdout a square with '#' character.

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

    def my_print(self):
        """
        Prints in stdout a square with '#' character.

            If 'self.__size' is equal to 0, prints an empty line.

            Otherwise, prints 'self.__size' number of rows,
            each containing 'self.__size' number of '#'
            characters followed by a newline character.

        Args:
            None

        Returns:
            None
        """

        if self.__size == 0:
            print()

        else:
            for row in range(self.__size):
                for col in range(self.__size):
                    print("#", end="")
                print()
