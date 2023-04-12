#!/usr/bin/python3

def uniq_add(my_list=[]):
    """This function adds all unique integers in a list

    Args:
        my_list: list to search

    Returns:
        Sum of the integers
    """

    sum = 0
    new_list = list(set(my_list))   # creating unique list with set()
    for index in range(len(new_list)):
        sum += new_list[index]

    return sum
