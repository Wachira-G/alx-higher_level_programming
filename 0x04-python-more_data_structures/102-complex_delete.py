#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    '''
    Deletes keys with a specific value in a dictionary.
    '''
    keys = []
    for key, valu in a_dictionary.items():
        if valu == value:
            keys.append(key)
    for key in keys:
        del a_dictionary[key]
    return a_dictionary
