#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """This function delete an item at a specific position in a list

    Args:
        my_list: the list to search
        idx: index of item to delete

    Return:
        New list after item has been deleted
    """

    if idx < 0 or idx > len(my_list):
        return my_list

    for index in range(len(my_list)):
        if idx == index:
            del my_list[idx]

    return my_list
