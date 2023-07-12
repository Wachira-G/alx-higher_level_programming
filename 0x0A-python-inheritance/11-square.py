#!/usr/bin/python3

'''A module defining a class Square
that inherits from Rectangle (9-rectangle.py).
(task based on 10-square.py).
'''

Square_ = __import__("10-square").Square


class Square(Square_):
    """a class extending the definition of a Square form task 10-square.py

    Args:
        Square_ (class): a class defining a Square
    """
    def __str__(self):
        """extends the derived class base method
         by replacing the name Rectangle with the name Square

        Returns:
            str: string representation of a Square,
             with the right name to match
        """
        new_name = "Square"
        return super().__str__().replace('Rectangle', new_name)
