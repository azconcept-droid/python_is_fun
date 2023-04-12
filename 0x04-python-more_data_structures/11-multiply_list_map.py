#!/usr/bin/python3

def multiply_list_map(my_list=[], number=0):
    """This function returns a list with all values multiplied by a number
       without using any loops, map must be used

    Args:
        my_list: list to search
        number: number used to multiply values

    Returns:
        New list
    """

    new_list = list(map(lambda x: x*number, my_list))
    return new_list
