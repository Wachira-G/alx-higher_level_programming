#!/usr/bin/python3

'''A module containing a function that inserts a line of text to a file,
after each line containing a specific string:
'''


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file
     after each line containing  a specific string

    Args:
        filename (str, optional): the file. Defaults to "".
        search_string (str, optional): the string were are searchng.
         Defaults to "".
        new_string (str, optional): the string to insert. Defaults to "".
    """
    with open(filename, encoding='utf-8') as file:
        lines = file.readlines()

    with open(filename, mode='w', encoding='utf-8') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
