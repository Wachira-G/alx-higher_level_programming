#!/usr/bin/python3

"""
This module defines the Square class
which is a subclass of the Rectangle class, a subclass of the Base class.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    '''
    '''
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self) -> str:
        rect_string = super().__str__()
        last_slash = rect_string.rfind('/')
        square_string = rect_string[:last_slash]
        return square_string.replace("Rectangle", "Square")

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the instance based on the given arguments.

        Args:
            *args is the list of arguments - no-keyworded arguments
                1st argument should be the id attribute
                2nd argument should be the size attribute
                3rd argument should be the x attribute
                4th argument should be the y attribute
            **kwargs can be thought of as a double pointer to a dictionary:
              key/value (keyworded arguments)
            **kwargs must be skipped if *args exists and is not empty
            Each key in this dictionary represents an attribute to the instance

        Returns:
            None
        """
        if args and len(args) > 0:
            size = len(args)

            if size > 0:
                self.id = args[0]

            if size > 1:
                self.size = args[1]

            if size > 2:
                self.x = args[2]

            if size > 3:
                self.y = args[3]

        elif kwargs:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'size':
                    self.size = value
                else:
                    private_attr = '_Rectangle__' + key
                    if hasattr(self, private_attr):
                        setattr(self, private_attr, value)

    def to_dictionary(self):
        """Creates a dicitonary represenation of the instance

        Returns:
            dict: a dict containing the instances's id, width, height, x and y
        """
        return {'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y,
                }
