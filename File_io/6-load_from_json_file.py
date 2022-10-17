#!/usr/bin/python3
"""This module declare a function that
loads obj from a json file
"""
import json


def load_from_json_file(filename):
    """
    read an obj from a json file format
    """

    with open(filename) as file:
        my_obj = json.load(file)
        return (my_obj)
