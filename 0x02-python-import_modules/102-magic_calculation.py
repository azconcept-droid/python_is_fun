#!/usr/bin/python3
from magic_calculation_102 import add, sub

def magic_calculation(a, b):
    """This function calculate in form of python bytecode

    Args:
        a: first integer
        b: second integer
    
    Return:
        The return value is c.
    """
    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return (c)
    else:
        c = sub(a, b)
        return c
