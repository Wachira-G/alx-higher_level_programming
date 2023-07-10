#!/usr/bin/python3

'''A module that demostrates how to change
the behavior of derived attributes'''


class MyInt(int):
    """A class that inherits from int:
    but is a rebel such that  MyInt has == and != operators inverted

    Args:
        int (int): is the base int class
    """
    def __eq__(self, __value: object) -> bool:
        """inverts the base method __eq__

        Args:
            __value (object): the object

        Returns:
            bool: true or false(inverted)
            on whether the instance is equal to the object
        """
        return not super().__eq__(__value)

    def __ne__(self, __value: object) -> bool:
        """inverts the base method __ne__

        Args:
            __value (object): the object

        Returns:
            bool: true or false(inverted) on whether
             the instance is not equal to the object
        """
        return not super().__ne__(__value)
