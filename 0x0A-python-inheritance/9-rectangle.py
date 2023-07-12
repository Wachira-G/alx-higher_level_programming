#!/usr/bin/python3

'''A module containing a class Rectangle that inherits from BaseGeometry
(7-base_geometry.py). (task based on 8-rectangle.py)
'''

Rectangle_ = __import__("8-rectangle").Rectangle


class Rectangle(Rectangle_):
    '''a class Rectangle that inherits from BaseGeometry
    (7-base_geometry.py). (task based on 8-rectangle.py)
    '''
    def area(self):
        """calculates the area of the rectangle

        Returns:
            int: the area of the reactangle
        """
        return self.__width * self.__height

    def __str__(self):
        """creates the string representation of a rectangle

        Returns:
            str: string representation of a rectangle
        """
        return '[Rectangle] {}/{}'.format(self.__width, self.__height)
