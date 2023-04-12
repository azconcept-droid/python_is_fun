#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    """This function return set of all elements present in only one sets

    Args:
        set_1: first set
        set_2: second set
    """

    return (set_1 ^ set_2)
