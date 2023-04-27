#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """This function prints x elements of a list

    Args:
        my_list (list): list to print
        x (int): number of elements to print

    Returns:
        The real number of elements printed
    """

    count = 0
    try:
        for i in range(x):
            print(my_list[i], end='')
            count += 1
    except (IndexError, TypeError):
        pass
    finally:
        print()

    return count