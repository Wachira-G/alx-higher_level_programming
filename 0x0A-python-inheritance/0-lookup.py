#!/usr/bin/python3

"""A module containing a function that returns a list of available attributes
and methods of an object

Methods:
    lookup: the function.
"""


def lookup(obj):
    """a function that returns the list of available attributes
     and methods of an object

    Args:
        obj (object): is the foundational structure
         that all other types inherite from (except Exception)

    Returns:
        list: a list of the available attribures and methods of an object
    """
    return dir(obj)
