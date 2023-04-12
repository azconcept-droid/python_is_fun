#!/usr/bin/python3

def multiple_returns(sentence):
    """This function returns two values

    Arg:
        sentence: the sentence to evaluate

    Returns:
        The length and the first letter of the sentence
    """
    length = len(sentence)
    if length == 0:
        first_letter = None
    else:
        first_letter = sentence[0]
    return (length, first_letter)
