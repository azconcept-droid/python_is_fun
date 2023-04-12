#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div

def is_operator(operator):
    """This function checks if operator is available

    Agrs:
        argv[2]: operator from command line arguments

    Returns:
        The True or False
    """
    operators = ["+", "-", "*", "/"]
    for sign in operators:
        if sign == operator:
            return True
    else:
        return False


def calculate(a, b, operator):
    """This function do the calculation and print result

    Agrs:
        a: first operand
        b: second operand
        operator: +, -, * or /.

    Returns:
        None.
    """
    if operator == "+":
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif operator == "-":
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif operator == "*":
        print("{} * {} = {}".format(a, b, mul(a, b)))
    elif operator == "/":
            print("{} / {} = {}".format(a, b, div(a, b)))


if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if is_operator(argv[2]):
        a = int(argv[1])
        b = int(argv[3])
        calculate(a, b, argv[2])
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)