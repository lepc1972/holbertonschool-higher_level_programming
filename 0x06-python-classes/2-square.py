#!/usr/bin/python3
""" Module that creates a class named square"""


class Square:
    """Square with private instance attribute and instantiation"""
    def __init__(self, size=0):
        """Initialize data"""
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
