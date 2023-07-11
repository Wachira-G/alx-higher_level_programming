#!/usr/bin/bash
import json

"""A module containing a funtion that creates an object from a JSON file"""


def load_from_json_file(filename):
    """creates an Object from a "JSON file"

    Args:
        filename (str): the JSON file

    Returns:
        object: the object from the json file
    """
    with open(filename, encoding="utf-8") as file:
        return json.load(file)
