#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """This funtion deletes keys with a specific value

    Args:
        a_dictionary (dict): dictionary to search
        value (any data type): value to search for

    Returns:
        New dictionary after the key:value have been deleted
    """

    new_dictionary = a_dictionary.copy()
    for key, val in new_dictionary.items():
        if value == val:
            del a_dictionary[key]

    return a_dictionary