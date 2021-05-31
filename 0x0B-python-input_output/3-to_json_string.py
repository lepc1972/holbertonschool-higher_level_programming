#!/usr/bin/python3
"""
Defining to_json_string function obj to json
"""
import json


def to_json_string(my_obj):
    '''
    function that returns the JSON representation of an object (string)
    '''
    return json.dumps(my_obj)
