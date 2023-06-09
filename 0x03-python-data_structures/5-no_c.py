#!/usr/bin/env python3
def no_c(my_string):
    '''Removes all characters c and C from a string.'''
    string_list = [char for char in my_string if char.lower() != 'c']
    return ''.join(string_list)
