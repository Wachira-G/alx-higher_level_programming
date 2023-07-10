#!/usr/bin/python3

"""A module that demonstrates inheritance
"""


def is_kind_of_class(obj, a_class) -> bool:
    """a funtion that returns True if the object is an instance of,
    or if the object is an instance of a class that inherited from,
     the specified class ; otherwise False."

    Args:
        obj (Any): the object
        a_class (Any): the class

    Returns:
        bool: true of false
    """
    return isinstance(obj, a_class)
