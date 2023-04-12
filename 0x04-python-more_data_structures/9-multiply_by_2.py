#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """This function multiply all values in a dictionary by 2

    Args:
        a_dictionary: dictionary to search

    Returns:
        New dictionary
    """

    new_dictionary = a_dictionary.copy()
    for key in a_dictionary:
        new_dictionary[key] = a_dictionary[key] * 2

    return new_dictionary
