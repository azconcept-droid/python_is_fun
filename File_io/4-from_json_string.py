#!/usr/bin/python3
"""
Module that returns python obj from string
"""
import json


def from_json_string(my_str):
    """
    This function returns python obj from string
    """

    return json.loads(my_str)