#!/usr/bin/python3
def best_score(a_dictionary):
    """This function returns a key with the biggest integer value

    Args:
        a_dictionary: dictionary to search
    """

    if a_dictionary == None:
        return None
    else:
        # The biggest is the max item in the list of values
        biggest_integer = max(a_dictionary.values())
        for key in a_dictionary:
            if a_dictionary[key] == biggest_integer:
                return key
