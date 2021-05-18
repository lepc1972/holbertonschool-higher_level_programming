#!/usr/bin/python3
"""Module that give us the square area"""


class Square:
    """Square with private instance attribute and instantiation"""
    def __init__(self, size=0):
        """Initialize data"""
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """This function return square area"""
        return (self.__size ** 2)
