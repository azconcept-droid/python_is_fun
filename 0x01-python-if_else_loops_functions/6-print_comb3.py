#!/usr/bin/python3
for x in range(0, 10):
    for y in range(0, 10):
        if x < y and x != y:
            if x == 8 and y == 9:
                print("{}{}".format(x, y))
                continue
            print("{}{}".format(x, y), end=', ')