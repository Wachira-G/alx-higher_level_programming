#!/usr/bin/python3
import json

"""A module containing a function that converts the json string
to a python data structure"""


def from_json_string(my_str):
    """returns an object (Python date structure) represented by a JSON string

    Args:
        my_str (str): the json string

    Returns:
        Any: the Python data structure object
    """
    return json.loads(my_str)
