#!/usr/bin/python3


class Square:
    """
    A class Square that defines a square by: (based on 2-square.py)
        Private instance attribute: size
        Instantiation with optional size: def __init__(self, size=0):
            size must be an integer, otherwise raise a TypeError exception
                with the message size must be an integer
            if size is less than 0, raise a ValueError exception
                with the message size must be >= 0
        Public instance method: def area(self):
            that returns the current square area
        """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        side = self.__size
        return side * side
