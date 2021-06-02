#!/usr/bin/python3
"""Module to know is instance of object or class"""


def is_kind_of_class(obj, a_class):
    """Function that checks of object is instance of, or if
    is instance of class that inherited from specified class
    Arguments:
        obj: object to be checked
        a_class: class to be checked
    Return: True or false
    """
    return (isinstance(obj, a_class))
