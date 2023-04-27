#!/usr/bin/python3
cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]

cast = {}
for name, height in zip(cast_names, cast_heights):
    cast[name] = height

"""Correction
cast = dict(zip(cast_names, cast_heights)) # replace with your code
"""
print(cast)