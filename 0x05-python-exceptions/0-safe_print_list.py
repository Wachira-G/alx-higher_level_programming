#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    '''Prints x elements in a list'''
    number = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            number += 1
        except IndexError:
            print()
            return number
    print()
    return number
