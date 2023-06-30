#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""This is a module extending module 5-square.

"""


class Square:
    """
    A class Square that defines a square by: (based on 5-square.py)
        Private instance attribute: size:
            property def size(self): to retrieve it
            property setter def size(self, value): to set it
                size must be an integer, otherwise raise a TypeError exception
                    with the message size must be an integer
                if size is less than 0, raise a ValueError exception
                    with the message size must be >= 0
        Instantiation with optional size and optional position:
          def __init__(self, size=0, position=(0, 0)):
        Public instance method: def area(self):
            that returns the current square area
        Public instance method: def my_print(self): that prints in stdout
        the square with the character #:
            if size is equal to 0, print an empty line
            position should be use by using space
              - Don’t fill lines by spaces when position[1] > 0
        Private instance attribute: position:
            property def position(self): to retrieve it
            property setter def position(self, value): to set it:
                position must be a tuple of 2 positive integers,
                otherwise raise a TypeError exception with the message
                'position must be a tuple of 2 positive integers'
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initializes Square class.

        Args:
            size (int): Size of Square.
            position (tuple): Position of Square.

        Attributes:
            __size (int): Size of Square.
            __position (tuple): Position of Square.

        """
        self.size = size
        self.position = position

    def area(self):
        """Calculates area of Square.

        Returns:
            int: Area of Square.

        """
        side = self.__size
        return side * side

    @property
    def size(self):
        """Getter method for size attribute.

        Returns:
            int: Size of Square.

        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for size attribute.

        Args:
            value (int): Value to set as size attribute.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.

        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Getter method for position attribute.

        Returns:
            tuple: Position of Square.

        """
        return self.__position

    @position.setter
    def position(self, value):
        """Setter method for position attribute.

        Args:
            value (tuple): Value to set as position attribute.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.

        """

        if not isinstance(value, tuple) \
                or len(value) != 2 \
                or not all(isinstance(i, int) for i in value) \
                or not all(i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")

        else:
            self.__position = value

    def my_print(self):
        """Prints Square using '#' character.

        If size is 0, prints an empty line.
        Position is used to print spaces before the Square.

        """
        side = self.__size
        pos = self.__position
        result = ''

        if self.__size == 0:
            return result

        else:
            result = '\n' * pos[1]
            result += side * (pos[0] * ' ' + side * '#' + '\n')
            return result.rstrip('\n')

    def __str__(self) -> str:
        """prints the class

        Returns:
            str: the string rep of the class
        """
        return self.my_print()
