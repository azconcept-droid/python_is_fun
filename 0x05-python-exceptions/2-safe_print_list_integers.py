#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """This function print the first x elements of a list and only intgers

    Args:
        my_list (list): list to search
        x (int): number of elements to print

    Returns:
        Number of elements printed
    """

    count = 0
    for i in range(x):
        try:
            display = "{:d}".format(my_list[i])
            print(display, end='')
            count += 1
        except (ValueError, TypeError):
            continue

    print()
    return count