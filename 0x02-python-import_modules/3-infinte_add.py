#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    add_all = 0
    for index in range(1, len(argv)):
        add_all = add_all + int(argv[index])
    print(add_all)
