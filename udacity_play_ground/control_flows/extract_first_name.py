#!/usr/bin/python3

names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

first_names = [name.lower().split(' ')[0] for name in names] # write your list comprehension here
"""correction
first_names = [name.split()[0].lower() for name in names]
"""
print(first_names)