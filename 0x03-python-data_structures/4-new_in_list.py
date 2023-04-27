#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """This function replaces an element in a list
       without altering the list

    Args:
        my_list: list to search
        idx: index of element to replace
        element: new element to put in replacement

    Return:
        Returns a copy of original list if idx is negative
        Returns a copy of original list if idx is out of range
        Returns new list
    """

    new_list = my_list[:]
    if idx < 0:
        return (new_list)
    if idx > len(my_list):
        return (new_list)
    index = range(len(my_list))
    for i in index:
        if idx == i:
            new_list[i] = element
    return (new_list)
