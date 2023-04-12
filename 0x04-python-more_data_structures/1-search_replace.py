#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """This function search and replace the occurrences of an element by another in anew list

    Args:
        my_list: list to searcb
        search: element to search  for
        replace: element to put in replacement

    Returns:
        New list with element replaced 
    """

    new_list = my_list[:]
    for index in range(len(my_list)):
        if my_list[index] == search:
            new_list[index] = replace

    return new_list
