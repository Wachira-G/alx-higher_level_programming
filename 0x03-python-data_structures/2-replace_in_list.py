#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """Replaces an element of a list at a specific position (like in C)."""
    size = len(my_list)
    if idx < 0:
        return my_list
    elif idx > size - 1:   # len starts from 1
        return my_list
    else:
        my_list[idx] = element
        return my_list
