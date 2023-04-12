#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """This function checks if a number is divisible by 2 in a list

    Args:
        my_list: list to search

    Return:
        New list of True or False depending on if the element at the same position
        in my_list is a multiple of 2 e.g new_list = [True, False, ...]
    """
    new_list = []
    for num in my_list:
        if num % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)

    return new_list
