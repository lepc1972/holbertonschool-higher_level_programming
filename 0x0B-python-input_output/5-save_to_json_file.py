#!/usr/bin/python3
"""
Defining function  save_to_json_file
"""
import json


def save_to_json_file(my_obj, filename=""):
    '''
    Function that writes an Object to a text file, using JSON
    '''
    with open(filename, mode="w", encoding="UTF-8") as fl:
        json.dump(my_obj, fl)
