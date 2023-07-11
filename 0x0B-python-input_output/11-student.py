#!/usr/bin/python3

"""A module defining a class that defines a student"""


class Student:
    """A class defining a student
    """

    def __init__(self, first_name, last_name, age) -> None:
        """initializes an instance of the class Student

        Args:
            first_name (str): the first name name
            last_name (str): the last name name
            age (int): the age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None) -> dict:
        """A function that returns the dictionary description
        with simple data structure
        (list, dictionary, string, integer and booolen)
        for JSON serialization of and object

        Args:
            obj (Any): the object

        Returns:
            dict: a dictionary of the object description
        """
        if isinstance(attrs, list) and all(isinstance(i, str) for i in attrs):
            al = {i: getattr(self, i) for i in attrs if hasattr(self, i)}
            return al
        else:
            return self.__dict__

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
