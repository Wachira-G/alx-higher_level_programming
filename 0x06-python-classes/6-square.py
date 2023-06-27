#!/usr/bin/python3


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
        self.__size = size
        self.__position = position

    def area(self):
        side = self.__size
        return side * side

    @property
    def size(self):
        # self.__getattribute__(self.__size)
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            # self.__setattr__(self.__size, value)
            self.__size = value

    @property
    def position(self):
        # self.__getattribute__(self.__size)
        return self.__position

    @position.setter
    def positon(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2 or any(
                not isinstance(i, int) or i < 0
                for i in value):
            raise ValueError("size must be >= 0")
        else:
            # self.__setattr__(self.__size, value)
            self.__position = value

    def my_print(self):
        side = self.__size
        area = side * side
        if self.__size == 0:
            print()
        else:
            for row in range(side):
                for item in range(side):
                    print("{}".format('#'), end='')
                print()

    @property
    def size(self):
        # self.__getattribute__(self.__size)
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            # self.__setattr__(self.__size, value)
            self.__size = value

    def my_print(self):
        side = self.__size
        area = side * side
        pos = self.__position
        if self.__size == 0:
            print()
        else:
            for row in range(side):
                if pos[0] > 0:
                    print("{}".format(pos[0]*' '), end='')
                for item in range(side):
                    print("{}".format('#'), end='')
                print()
