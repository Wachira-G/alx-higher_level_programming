#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    '''Finds all multiples of 2 in a list.
        Return a new list with True or False,
        depending on whether the integer at the same position
        in the original list is a multiple of 2'''
    is_2_multiple = [item % 2 == 0 for item in my_list]
    return is_2_multiple
