#!/usr/bin/python3
"""This module declare a function that
saves an obj in json file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    write an obj in a json file format
    """

    with open(filename, mode='w') as file:
        json.dump(my_obj, file)
