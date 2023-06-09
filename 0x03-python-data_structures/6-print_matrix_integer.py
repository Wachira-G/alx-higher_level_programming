#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    '''Prints a matrix of integers.'''
    for row in matrix:
        row_format = ' '.join(['{}'] * len(row))  # == '{} {}' if len = 2
        print(row_format.format(*row))  # the '*' is sequence unpacking
