#!/usr/bin/python3
import json

"""A module containing a function
that returns the JSON rep of an object(string)
"""


def to_json_string(my_obj):
    """converts a string to a json representation

    Args:
        my_obj (str): string we want to convert

    Returns:
        str: the json representation
    """
    return json.dumps(my_obj)
