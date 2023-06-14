def square_matrix_simple(matrix=[]):
    '''Computes the square value of all integers of a matrix

        Returns a new matrix which is same size, with each value
    being the square of the values of the input'''

    square_matrix = []
    for row in matrix:
        square_matrix.append(list(map((lambda x: x ** 2), row)))
    return square_matrix
