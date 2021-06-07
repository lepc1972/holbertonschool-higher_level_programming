#!/usr/bin/python3
"""Module for Base Class"""


import json
import os
import models


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

    @classmethod
    def save_to_file(cls, list_objs):
        """writes JSON representation of list_objs to a file"""
        list_dict = []
        if list_objs:
            for i in list_objs:
                list_dict += [i.to_dictionary()]
        with open(cls.__name__ + '.json', 'w', encoding='utf-8') as f:
            f.write(cls.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """return the list of JSON string representation"""
        empty = []
        if json_string is None or not json_string:
            return empty
        else:
            load = json.loads(json_string)
            return load

    
    @classmethod
    def create(cls, **dictionary):
        """
        Returns:
            An instance with all attributes already set.
        """
        if cls.__name__ == 'Rectangle':
            dummy_shape = cls(3, 7, 5, 8)
        if cls.__name__ == 'Square':
            dummy_shape = cls(3, 7, 5)
        dummy_shape.update(dummy_shape, **dictionary)
        return dummy_shape

    @classmethod
    def load_from_file(cls):
        name = cls.__name__ + '.json'
        emptylist = []
        list3 = []
        try:
            with open(name, mode='r', encoding='UTF8') as xfile:
                aux = xfile.read()
                emptylist = cls.from_json_string(aux)
                """List of dicts"""
                for elem in emptylist:
                    aux2 = cls.create(**elem)
                    list3.append(aux2)
                return list3
        except FileNotFoundError:
            return emptylist
