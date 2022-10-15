#!/usr/bin/python3
"""
Module that returns the JSON representation of an object (string)
"""
import json

def to_json_string(my_obj):
    """
    This function returns JSON rep of an obj
    """

    return json.dumps(my_obj)
