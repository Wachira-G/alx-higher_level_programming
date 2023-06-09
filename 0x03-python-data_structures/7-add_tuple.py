#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    '''Adds 2 tuples.

        Returns a tuple with 2 integers:
            First element is the addition of the 1st element of each argument
            Second element is the addition of the 2nd element of each argument
    '''
    tuple_a = tuple([tuple_a[a] if a < len(tuple_a) else 0 for a in range(2)])
    tuple_b = tuple([tuple_b[b] if b < len(tuple_b) else 0 for b in range(2)])
    first_elem = tuple_a[0] + tuple_b[0]
    second_elem = tuple_a[1] + tuple_b[1]
    return first_elem, second_elem
