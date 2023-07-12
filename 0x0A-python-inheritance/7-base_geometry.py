#!/usr/bin/python3

''' A module implementing a simple class
'''


class BaseGeometry:
    """a simple class
    """
    def area(self):
        """a simple area method

        Raises:
            Exception: does just that
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value

        Args:
            name (str): the name of the value
            value (int): the value

        Raises:
            TypeError: if value is not of type int
            ValueError: if value is zero or less
        """
        if not type(value) == int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
