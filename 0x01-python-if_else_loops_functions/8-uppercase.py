#!/usr/bin/python3

def uppercase(str):
    "Converts string to uppercase letter"

    for c in str:   # for each character in string
        if ord(c) >= 97 and ord(c) < 123:
            new_chr = chr(ord(c) - 32)
        else:
            new_chr = c
        print("{:s}".format(new_chr), end='')
    print()
