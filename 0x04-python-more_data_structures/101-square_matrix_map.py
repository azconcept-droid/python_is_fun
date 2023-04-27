#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    """This function computes the square value of all integers of a matrix

    Args:
        matrix: the matrix

    Returns:
        A new matrix with square of the value of the input

    new_matrix = []
    for row in matrix:
        new_row = []
        for integer in row:
            new_integer = integer**2
            new_row.append(new_integer)
        new_matrix.append(new_row)
    """
    new_matrix = list(map(lambda x: x**2, matrix))
    return new_matrix
