#!/usr/bin/python3
"""
Defining from_json_string
"""
import json


def from_json_string(my_str):
    '''
    Function that returns an object represented by a JSON string:
    '''
    return json.loads(my_str)
