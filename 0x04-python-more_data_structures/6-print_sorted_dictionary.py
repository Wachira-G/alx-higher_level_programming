#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    '''
    Prints a dictionary by ordered keys (of the first level)
    in alphabetic order.
    '''
    keys = sorted(a_dictionary)
# use key=str.casefold parameter.
# In Python, when sorting strings, uppercase letters
# are considered to have a lower value than lowercase letters.
    for key in keys:
        print('{}: {}'.format(key, a_dictionary[key]))
