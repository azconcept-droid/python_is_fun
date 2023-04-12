#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """This function print list in reverse

    Args:
        my_list: list to reverse
    """
    for item in reversed(my_list):
        print("{}".format(item))
