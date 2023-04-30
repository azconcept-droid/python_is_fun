#!/usr/bin/python3
from sys import stderr
def safe_function(fct, *args):
    """This funtion that executes a function safely

    Args:
        fct (object): funtion name
        *args (arguments): function arguments

    Returns:
        result of the function
    """

    try:
        result = fct(*args)
    except Exception as e:
        result = None
        stderr.write("Exception: {}\n".format(e))
    finally:
        return result
