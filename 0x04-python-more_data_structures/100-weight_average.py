#!/usr/bin/python3
def weight_average(my_list=[]):
    """This function calculate the weighted average of all integers tuple

    Args:
        my_list: list of tuples

    Returns:
        Zero if list is empty
        else return the weighted average
    """

    summation_fx = 0
    summation_f = 0
    for score, weight in my_list:
        summation_fx += score * weight
        summation_f += weight

    weighted_average = summation_fx / summation_f

    return weighted_average
