#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Replaces an element in a list at a specific position
        without modifying the original list (like in C)."""
    size = len(my_list)
    copy = my_list[:]
    if idx < 0:
        return copy
    elif idx > size - 1:   # len starts from 1
        return copy
    else:
        copy[idx] = element
        return copy
