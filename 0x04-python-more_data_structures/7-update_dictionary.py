#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """This function replaces or adds key/value in a dictionary

    Args:
        a_dictionary: dictionary to search
        key: item key
        value: item value

    Returns:
        Updated dictionary
    """

    for keys in a_dictionary:
        if keys == key:
            a_dictionary[key] = value
            break
    if key not in a_dictionary:
        a_dictionary[key] = value

    return a_dictionary
