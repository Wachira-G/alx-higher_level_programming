#!/usr/bin/python3

"""A module that defines a function that adds a new attribute
 to an object if it possible
"""


def add_attribute(self, name, value):
    """a function that adds a new attribute to an object if it's possible

    Args:
        name (str): the name of the object
        value (Any): any of the types that can be stored there.
    """
    if not hasattr(self, '__dict__'):
        raise TypeError("can't add new attribute")

    setattr(self, name, value)
