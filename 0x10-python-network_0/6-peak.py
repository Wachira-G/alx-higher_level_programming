#!/usr/bin/python3
"""A module defininng a peak finding function"""


def find_peak(list_of_integers):
    """Find a peak in a list of unsorted integers.

    Attributes:
      list_of_integers (list): a list of unsorted integers.
    Returns:
      the peak on the list or None if list is empty
    """
    if not list_of_integers:
        return None
    return max(list_of_integers)
