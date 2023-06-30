#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""A module that defines a class that defines a node of a singly linked list,
 and a class that defines a singly linked list.

This module provides the `Node` class
which represents a node of a singly linked list,
and the `SinglyLinkedList` class
which represents the singly linked list itself.

Attributes:
    None

Raises:
    TypeError: When the next_node is not None or a Node object.
    TypeError: When the data is not an integer.

Returns:
    None
"""


class Node:
    """A class that defines a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """Instantiates a new Node object with specified data and next_node.

        Args:
            data (int): The data for the node.
            next_node (Node, optional): The next node in the linked list.
              Defaults to None.

        Raises:
            TypeError: If the data is not an integer.

        Returns:
            None
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """Getter method to retrieve the value of data attribute.

        Args:
            None

        Returns:
            int: The value of data attribute.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """Setter method to set the value of data attribute.

        Args:
            value (int): The new value for data attribute.

        Raises:
            TypeError: If the value is not an integer.

        Returns:
            None
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")

        self.__data = value

    @property
    def next_node(self):
        """Getter method to retrieve the value of next_node attribute.

        Args:
            None

        Returns:
            Node: The value of next_node attribute.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value=None):
        """Setter method to set the value of next_node attribute.

        Args:
            value (Node, optional): The new value for next_node attribute.
              Defaults to None.

        Raises:
            TypeError: If the value is not None or a Node object.

        Returns:
            None
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")

        self.__next_node = value


class SinglyLinkedList:
    """A class that defines a singly linked list."""
    def __init__(self):
        """Instantiates a new SinglyLinkedList object
          with an initial head node.

        Args:
            None

        Returns:
            None
        """
        self.head: Node = Node(0)

    def __str__(self):
        """Returns a string representation of the linked list.

        Args:
            None

        Returns:
            str: A string representation of the linked list.
        """
        current = self.head.next_node
        values = []

        while current is not None:
            values.append(str(current.data))
            current = current.next_node

        return '\n'.join(values)

    def sorted_insert(self, value):
        """Inserts a new Node into the correct sorted position
          in the list (in increasing order).

        Args:
            value (int): The value of the new node to be inserted.

        Raises:
            TypeError: If the value is not an integer.

        Returns:
            None
        """
        new_node: Node = Node(value)
        current: Node = self.head

        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node
