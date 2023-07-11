#!/usr/bin/python3
"""A module containing a function that returns the dictionary description"""


def class_to_json(obj):
    """A function that returns the dictionary description
    with simple data structure (list, dictionary, string, integer and booolen)
    for JSON serialization of and object

    Args:
        obj (Any): the object

    Returns:
        dict: a dictionary of the object description
    """
    return obj.__dict__
