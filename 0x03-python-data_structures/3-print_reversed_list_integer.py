#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    '''Prints all integers of a list, in reverse order.'''
    my_list.copy.reverse()
    for item in my_list:
        print('{:d}'.format(item))
