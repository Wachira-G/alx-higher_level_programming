#!/usr/bin/python3

"""A module demonstrating a basic file opening procedure in python
"""


def read_file(filename=""):
    """A function that reads a file and prints it to the stdout

    Args:
        filename (str, optional): the file wer are reading. Defaults to ""
    """
    with open(filename, encoding="utf-8") as file:
        print(file.read())
