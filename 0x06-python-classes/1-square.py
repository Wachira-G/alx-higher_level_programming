#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""This module extends the 0-square module.
It adds the init method to it.
"""


class Square:
    """A class representing a square.

    Attributes:
        __size (int): The size of a side of the square.
    """

    def __init__(self, size):
        """Initializes an instance of the Square class.

        Args:
            size (int): The size of a side of the square.

        Returns:
            None
        """
        self.__size = size
