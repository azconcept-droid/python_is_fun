#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """This function replace element at an index

    Args:
        my_list: list to search
        idx: index of element to replace
        element: new element to put in replacement

    Return:
        Returns original list if index is negative
        Returns original list if index is out of range
        Returns new list if index is within range.
    """

    if idx < 0:
        return (my_list)
    if idx > len(my_list):
        return (my_list)
    index = range(0, len(my_list))
    for i, item in zip(index, my_list):
        if idx == i:
            my_list[i] = element
    return (my_list)