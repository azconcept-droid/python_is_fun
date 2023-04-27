#!/usr/bin/python3
def safe_print_integer(value):
    """This function prints integer without error

    Args:
        value (all datatype): value to print

    Returns:
        True if value is an integer
        False if not
    """

    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        return False
