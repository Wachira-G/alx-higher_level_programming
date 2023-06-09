#!/usr/bin/python3
def max_integer(my_list=[]):
    '''Finds the biggest integer of a list.'''
    if len(my_list) == 0:
        max_number = None
    else:
        max_number = my_list[0]
        for item in my_list:
            if item > max_number:
                max_number = item
    return max_number
