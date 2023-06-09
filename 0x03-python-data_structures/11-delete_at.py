#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    '''Deletes the item at a specific position in a list.'''
    size = len(my_list)
    if idx > size - 1 or idx < 0:
        return my_list
    else:
        del my_list[idx]
        return my_list
