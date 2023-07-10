#!/usr/bin/python3

'''A module that defines a  function that returns
whether an object is an instance of a class or not'''


def is_same_class(obj, a_class):
    '''A function that returns True if the object is 'exactly' an instance
    of the specified class ; otherwise False.'''
    return type(obj) is a_class
