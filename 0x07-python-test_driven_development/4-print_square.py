#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""prints a square with the character '#'."""


def print_square(size):
    """Prints a square with the character '#'

    Args:
        size (int | float): the size of a side of the square

    Raises:
        TypeError: when size is not an integer
        ValueError: whns size is less than 0
    """
    # size is the size length of the square
    if not isinstance(size, (int, float)):
        raise TypeError("size must be an integer")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        size = int(size)
        for column in range(size):
            for row in range(size):
                print("#", end="")
            print()
