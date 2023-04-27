#!/usr/bin/python3

scores = {
             "Rick Sanchez": 70,
             "Morty Smith": 35,
             "Summer Smith": 82,
             "Jerry Smith": 23,
             "Beth Smith": 98
          }

passed = [name for name in scores if scores[name] >= 65] # write your list comprehension here
# Correction
# passed = [name for name, score in scores.items() if score >= 65]
print(passed)