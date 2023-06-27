#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""This module extends the 0-square module.
It adds an __init__ method that initializes an instance of Square class.
"""


class Square:
    """A class representing a square.

    Attributes:
        __size (int): The size of a square object.
    """

    def __init__(self, size=0):
        """Initializes an instance of the Square class.

        Args:
            size (int): The size of a side of the square.

        Returns:
            None

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than or equal to 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
