def print_matrix_integer(matrix=[[]]):
    """This function print matrix

    Arg:
        matrix: the matrix to print
    """

    for row in matrix:
        for col in row:
            print(str(col) + ' ', end='')
        print()
    