#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""This module contatins the add_integer function
The modules takes two pareameters a and b
which must be of either float or int type and casts them into integers,
then calcultates the addition of the two and finally returns the value
"""


def add_integer(a, b=98):
    """The function add_integer adds two integers
    (all floats are casted into integers) and returns the result

    Args:
        a (int): first argument of either int or float
        b (int, optional): second argumentst that is either an int or float.
            Defaults to 98.

    Raises:
        TypeError: if a is not an integer or a float, complain
        TypeError: if b is not an integer of a float, complain

    Returns:
        int: the result of the addition of the two values
    """
    if not isinstance(a, (int, float, bool)):
        raise TypeError("a must be an integer")

    elif not isinstance(b, (int, float, bool)):
        raise TypeError("b must be an integer")

    else:
        return int(a) + int(b)
