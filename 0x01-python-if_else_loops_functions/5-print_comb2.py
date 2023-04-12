#!/usr/bin/python3
for num in range(0, 100):
    if num == 99:
        print(num)
        continue
    print("{:d}".format(num), end=', ')
