#!/usr/bin/python3

"""
This module defines the Rectangle class which is a subclass of the Base class.
"""

from models.base import Base


class Rectangle(Base):
    """
    This class represents a rectangle and inherits from the Base class.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle object.

        Parameters:
        - width (int): The width of the rectangle.
        - height (int): The height of the rectangle.
        - x (int): The x-coordinate of the top-left corner
          of the rectangle. Default is 0.
        - y (int): The y-coordinate of the top-left corner
          of the rectangle. Default is 0.
        - id (int): The ID of the rectangle. Default is None.

        Raises:
        - TypeError: If width, height, x or y are not integers or floats.
                     If width or height are negative numbers.

        Returns:
        - None
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        Getter method for width attribute.

        Returns:
         - int: The width of the rectangle.
         """

        return self.__width

    @width.setter
    def width(self, width):
        """
        Setter method for width attribute.

        Parameters:
        - width (int): The new value for the width attribute.

        Raises:
        - TypeError: If width is not an integer or float.
                       If width is a negative number.

        Returns:
        - None
        """

        if not isinstance(width, int) or width is None:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """
        Getter method for height attribute.

        Returns:
        - int: The height of the rectangle.
        """

        return self.__height

    @height.setter
    def height(self, height):
        """
        Setter method for height attribute.

        Parameters:
        - height (int): The new value for the height attribute.

        Raises:
        - TypeError: If height is not an integer or float.
                      If height is a negative number.

        Returns:
        - None
         """

        if not isinstance(height, int) or height is None:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """
        Getter method for x attribute.

        Returns:
        - int: The x-coordinate of the top-left corner
          of the rectangle.
        """

        return self.__x

    @x.setter
    def x(self, x):
        """
        Setter method for x attribute.

        Parameters:
        - x (int): The new value for the x attribute.

        Raises:
        - TypeError: If x is not an integer or float.

        Returns:
        - None
        """

        if not isinstance(x, int) or x is None:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """
        Getter method for y attribute.

        Returns:
        - int: The y-coordinate of the top-left corner
          of the rectangle.
        """

        return self.__y

    @y.setter
    def y(self, y):
        """
        Setter method for y attribute.

        Parameters:
        - y (int): The new value for the y attribute.

        Raises:
        - TypeError: If y is not an integer or float.

        Returns:
        - None
        """

        if not isinstance(y, int) or y is None:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Calculates the area of a rectangle instance

        Returns:
            int: the area of the rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
        Displays the rectangle using '#' characters.

        Returns:
            None.
        """
        for _ in range(self.__height):
            print('#' * self.__width)

    def __str__(self) -> str:
        """
        Returns a string representation of the Rectangle.

        The string representation follows the format:
        "[Rectangle] (<id>) <x>/<y> - <width>/<height>"

        Returns:
        - str: A string representation of the Rectangle.
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)
