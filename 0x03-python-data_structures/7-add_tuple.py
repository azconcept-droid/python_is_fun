#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """This function adds 2 tuples together

    Args:
        tuple_a: first tuple
        tuple_b: second tuple

    Return:
        Returns a tuple with 2 integers
        e.g (1, 89) + (88, 11) = (89, 100)
    """

    # tuple_a = () and tuple_b = ()
    if len(tuple_a) == 0 and len(tuple_b) == 0:
        return ()
    # tuple_a = (3, ) and tuple_b = ()
    elif len(tuple_a) == 1 and len(tuple_b) == 0:
        new_tuple = (tuple_a[0], 0)
    # tuple_a = () and tuple_b = (2, )
    elif len(tuple_a) == 0 and len(tuple_b) == 1:
        new_tuple = (0, tuple_b[0])
    # tuple_a = (2, 5) and tuple_b = ()
    elif len(tuple_a) == 2 and len(tuple_b) == 0:
        return tuple_a
    # tuple_a = () and tuple_b = (2, 5)
    elif len(tuple_a) == 0 and len(tuple_b) == 2:
        return tuple_b
    # tuple_a = (7, 6) and tuple_b = (2. )
    elif len(tuple_a) == 2 and len(tuple_b) == 1:
        new_tuple = (tuple_a[0]+tuple_b[0], tuple_a[1])
    # tuple_a = (7, ) and tuple_b = (2. 5)
    elif len(tuple_a) == 1 and len(tuple_b) == 2:
        new_tuple = (tuple_a[0]+tuple_b[0], tuple_b[1])
    # tuple_a = (7, 6) and tuple_b = (2. 6) and other cases
    else:
        new_tuple = (tuple_a[0]+tuple_b[0], tuple_a[1]+tuple_b[1])

    return new_tuple
