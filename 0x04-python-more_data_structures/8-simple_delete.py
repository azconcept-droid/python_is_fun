#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """This function delete an item in a dictionary

    Args:
        a_dictionary: dictionary to search
        key: key of item to delete

    Returns:
        updated dictionary
    """

    for keys in a_dictionary:
        if keys == key:
            del a_dictionary[key]
            break

    return a_dictionary
