#!/usr/bin/python3

"""A module demonstrating inheritance
"""


class MyList(list):
    """The class MyList inherits from list

    Args:
        list (list): inherits from the list object class
    """

    def print_sorted(self):
        """A public method that prints the list sorted in ascending order.
        assuming that all the lelmetns are of type int.
        """
        print(sorted(self))
