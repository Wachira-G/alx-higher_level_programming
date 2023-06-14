#!/usr/bin/python3


def best_score(a_dictionary):
    '''
    Returns a key with the biggest integer value or None if no score is found.
    '''
    if a_dictionary:
        return max(a_dictionary, key=a_dictionary.get)
    else:
        return None
