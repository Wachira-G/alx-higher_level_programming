#!/usr/bin/python3
import json

"""A module containing a function that writes an object to a text file"""


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using a JSON representation

    Args:
        my_obj (Any): the object were want to write into file
        filename (str): the file we want to write into
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
