#!/usr/bin/python3
def print_list_integer(my_list=[]):
    ''' Prints all integers of a list,
        assume that the list only contains integers'''
    for item in my_list:
        print('{:d}'.format(item))
