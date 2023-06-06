#!/usr/bin/python3
def remove_char_at(str, n):
    """ creates a copy of the string, removing the character at the position n
        (not the Python way, the “C array index”). """
    if not n < 0:
        str = str[:n] + str[n+1:]
    return str
