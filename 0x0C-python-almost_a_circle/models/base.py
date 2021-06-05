#!/usr/bin/python3
"""Module for Base Class"""


import json
import os


class Base():
    """Main class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """function that initialize obj for testing"""
        if id == None:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id
