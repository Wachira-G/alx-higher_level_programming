#!/usr/bin/python3

"""A module demostrating a basic file write procedure (overwriting)
"""


def write_file(filename="", text=""):
    """Writes a string to a text file (utf8)

    Args:
        filename (str, optional): the file we are writing to. Defaults to "".
        text (str, optional): the text we are writing to the file.
          Defaults to "".

    Returns:
        _type_: the number of characters written
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        written = file.write(text)
        return written
