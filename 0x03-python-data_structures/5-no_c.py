#!/usr/bin/python3
def no_c(my_string):
    """This function removes the character c & C from a string

    Args:
        my_string: string to remove c and C

    Return:
        Returns the new string without c and C.
    """

    for idx, char in zip(range(0, len(my_string)), my_string):
        if char == 'C' or char == 'c':
            my_string = my_string[:idx] + my_string[idx + 1:]
            #print(idx, char)
        print(my_string)
    print()
    return (my_string)
