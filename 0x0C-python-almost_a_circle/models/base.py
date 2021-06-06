#!/usr/bin/python3
"""Module for Base Class"""


import json
import os


class Base():
    """Main class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """function that initialize obj for testing"""
        if id is None:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) <= 0:
            return ("[]")
        else:
            return (json.dumps(list_dictionaries))
