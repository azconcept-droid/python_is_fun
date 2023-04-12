#!/usr/bin/python3
def max_integer(my_list=[]):
    """This function finds the biggest integer of a list

    Arg:
        my_list: list to search

    Return:
        the highest value in the list
    """

    # Length of list
    if len(my_list) == 0:
        return None
    # Sort list in ascending order without changing the original list
    sorted_list = sorted(my_list)
    # The last integer in sorted_list is the biggest
    max = sorted_list[len(my_list) - 1]

    return max
