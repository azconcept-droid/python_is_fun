#!/usr/bin/python3
def element_at(my_list, idx):
    """This function pop element at particular index

    Args:
        my_list: list to search
        idx: element index

    Return:
        The return value is None if index is negative
        The return value is None if index is out of range
        Returns the element at that index.
    """
    if idx < 0 or idx > len(my_list):
        return None
    for index, item in zip(range(0, len(my_list)), my_list):
        if idx == index:
            return (my_list[index])
