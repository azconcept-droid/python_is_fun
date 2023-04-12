def print_matrix_integer(matrix=[[]]):
    """This function print matrix

    Arg:
        matrix: the matrix to print
    """

    if matrix == [[]]:
        print(end='')
    for row in matrix:
        for col in row:
            print(col, end=' ')
        print()
    