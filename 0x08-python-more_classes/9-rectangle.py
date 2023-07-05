#!/usr/bin/python3

"""A module for working with rectangles.

This module provides a class, Rectangle, that represents a rectangle
and provide methods to calculate its area and perimeter as well
as its string representation

Example usage:
    rect = Rectangle(5, 10)
    print(rect.area())  # Output: 50
    print(rect.perimeter())  # Output: 30
"""


class Rectangle:
    """A class representing a rectangle.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.

    Methods:
        area(): Returns the area of the rectangle.
        perimeter(): Returns the perimeter of the rectangle.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle instance.

        Args:
            width (int): The width of the rectangle. Defaults to 0.
            height (int): The height of the rectangle. Defaults to 0.
        """
        Rectangle.number_of_instances += 1

        self.width = width
        self.height = height

    @property
    def width(self):
        """Get or set the width of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle.

        Args:
            value (int): The new width value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Get or set the height of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle.

        Args:
            value (int): The new height value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.

        Methods:
            area(): Returns the area of the rectangle.
            perimeter(): Returns the perimeter of the rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self) -> int:
        """Calculates and returns the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self) -> int:
        """Calculate and return the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0

        return 2 * (self.__width + self.__height)

    def __str__(self) -> str:
        """
        Returns a string representation of the rectangle.

        Returns:
            str: A string representation of the rectangle.
        """
        str_rectangle = (
            self.__width * str(self.print_symbol) + "\n") * (self.__height - 1)
        str_rectangle += self.__width * str(self.print_symbol)
        return str_rectangle

    def __repr__(self) -> str:
        """Returns a string representation of the rectangle.

        Returns:
            str: A string representation of the rectangle.
        """
        return f"Rectangle({self.__width:d}, {self.__height:d})"

    def __del__(self) -> None:
        """Prints a message when an instance of Rectangle is deleted
        """
        Rectangle.number_of_instances -= 1

        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        """
        Determines which of the two rectangles has a greater area
        or if they are equal.

        Args:
            rect_1 (Rectangle): The first rectangle to compare.
            rect_2 (Rectangle): The second rectangle to compare.

        Returns:
            Rectangle: The rectangle with a greater area
            or if they have equal areas, either rectangle.

        Raises:
            TypeError: If rect_1 is not an instance of Rectangle.
            TypeError: If rect_2 is not an instance of Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        """Create a new instance of Rectangle with equal width and height.

        This method creates a new instance of the Rectangle class
        with both the width and height set to the given size,
        or 0 if no size is provided.

        Args:
            size (int): The size of the square. Defaults to 0.

        Returns:
            Rectangle: A new instance of the Rectangle class
            representing a square.

        Example:
            square = Rectangle.square(5)
            print(square.width)  # Output: 5
            print(square.height)  # Output: 5
        """
        return cls(size, size)
