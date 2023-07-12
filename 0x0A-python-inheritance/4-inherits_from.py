#!/usr/bin/python3

'''A module containing a fucntion that checks
if an objects is an instance of a base class'''


def inherits_from(obj, a_class):
    """checks if an object is an instance of a class
     that inherited (directly or indirectly) from the 'a_class'

    Args:
        obj (Any): the object
        a_class (any): the class

    Returns:
        bool: true or false
    """
    return type(obj) is not a_class and isinstance(obj, a_class)
