#!/usr/bin/python3
def safe_print_division(a, b):
    """This function divides 2 integers and print results

    Args:
        a (int): first number
        b (int): second number

    Return:
        Result of the division
    """

    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
        return result
