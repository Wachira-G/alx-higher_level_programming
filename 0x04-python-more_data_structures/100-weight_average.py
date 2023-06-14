#!/usr/bin/python3


def weight_average(my_list=[]):
    '''Return the weighted average of all integers tuple.'''
    if not my_list:
        return 0
    else:
        try:
            numerator = sum([row[0] * row[1] for row in my_list])
            denominator = sum([row[1] for row in my_list])
            weighted_average = numerator / denominator
        except ZeroDivisionError:
            return 0
    return weighted_average
