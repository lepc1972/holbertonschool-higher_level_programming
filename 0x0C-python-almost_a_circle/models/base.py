#!/usr/bin/python3
"""Module for Base Class"""


import json
import os
import models
import csv



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
        dummy_shape.update(**dictionary)
        return dummy_shape

    @classmethod
    def load_from_file(cls):
        """give us list of instances"""
        return_dict = []
        if os.path.exists(cls.__name__ + ".json"):
            with open(cls.__name__ + ".json", 'r', encoding='utf-8') as f:
                list_dict = cls.from_json_string(f.read())
                for dict in list_dict:
                    return_dict.append(cls.create(**dict))
        return (return_dict)

    @classmethod
    def load_from_file_csv(cls):
        """Load a list of instances from a CSV table"""

        if not os.path.exists(cls.__name__ + '.csv'):
            return []
        if cls.__name__ == 'Rectangle':
            attrs = ('id', 'width', 'height', 'x', 'y')
        elif cls.__name__ == 'Square':
            attrs = ('id', 'size', 'x', 'y')
        with open(cls.__name__ + '.csv', 'rt', newline='') as file:
            reader = csv.reader(file)
            objects = list(reader)
        objects = ((int(i) for i in l) for l in objects)
        return [cls.create(**dict(zip(attrs, l))) for l in objects]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Save a CSV version of the objects in list_objs for a class"""

        if list_objs is None:
            list_objs = []
        if cls.__name__ == 'Rectangle':
            attrs = ('id', 'width', 'height', 'x', 'y')
        elif cls.__name__ == 'Square':
            attrs = ('id', 'size', 'x', 'y')
        list_objs = ([getattr(o, a) for a in attrs] for o in list_objs)
        with open(cls.__name__ + '.csv', 'wt', newline='') as file:
            writer = csv.writer(file)
            for row in list_objs:
                writer.writerow(row)
