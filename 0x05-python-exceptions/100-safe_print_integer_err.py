#!/usr/bin/python3
from sys import stderr
def safe_print_integer_err(value):
    """This function prints an integer without error

    Args:
        value (int, string etc): value to print

    Returns:
        True if value has been correctly printed else False
    """

    try:
        print("{:d}".format(value))
        return True
    except Exception as e:
        stderr.write("Exception: {}\n".format(e))
        return False
