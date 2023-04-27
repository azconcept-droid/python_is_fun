#!/usr/bin/python3

def roman_to_int(roman_string):
    """This function converts a Roman numeral to an integer
    I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000 
    Args:
        roman_string: the Roman numeral to convert

    Returns:
        Roman numeral in integer format
        or 0 if roman_string is not a string or None
    """

    if roman_string == None:
        return 0
    if type(roman_string) != str:
        return 0

    roman_numerals = { 'I': 1, 'V': 5, 'X': 10, 'L': }