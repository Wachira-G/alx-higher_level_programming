#!/usr/bin/python3

"""
A module containing a class that forms the base for all other classes.
It instantiates the id attribute for each instance.
"""


class Base:
    """
    Is a base for all other classes of this project.
    Manages the id attribute in all the future classes
    to avoid duplicating the same code.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        A class constructor that assigns an id to an instance
        and increments the number of instances in the class.

        Args:
            id (int): Identifies an instance uniquely.
        """

        if id is not None:
            self.id = id  # Assume id is an int and no need to test its type

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
