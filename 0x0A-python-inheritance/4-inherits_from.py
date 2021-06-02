#!/usr/bin/python3
"""Module for sub class function"""


def inherits_from(obj, a_class):
    """Function that recturns True if the object is instance of a class that
    inherited (directly or indirectly) from the specified class
    Arguments:
        obj: object to check
        a_class: class to be checked
    Return:
        True or false
    """
    if type(obj) is a_class:
        return (False)
    return issubclass(type(obj), a_class)
