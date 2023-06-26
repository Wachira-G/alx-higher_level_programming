#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    '''prints the first x elements of a list and only integers.'''
    number = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            number += 1
        except ValueError:
            pass
        except TypeError:
            pass
    print()
    return number
