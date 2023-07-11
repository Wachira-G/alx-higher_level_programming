#!/usr/bin/python3

'''A module containing a function that returns a list of lists of integers
representing the Pascal's triangle of n'''


def pascal_triangle(n):
    '''A fucntion that creates a pascal's triangle.
     Args:
      n (int): the size of the triangle

    Return: (list): a list containing list of integers rep pascal triangle
      or empty list if size is zero
    '''
    triangle = []

    if n == 0:
        return []

    elif n == 1:
        triangle.append([1])
        return triangle

    else:
        triangle = pascal_triangle(1)

        prev = triangle[-1]
        i = 0
        while i < n - 1:
            new = []
            new.append(1)

            j = 0
            while j < i:
                new.append(prev[j] + prev[j + 1])
                j += 1

            new.append(1)

            triangle.append(new)
            prev = triangle[-1]
            i += 1

        return triangle
