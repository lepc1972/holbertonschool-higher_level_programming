#!/usr/bin/python3
"""Python source code that produces exact byte code"""


import math


class MagicClass:
    """class to create bytecode in python"""
    def __init__(self, radius=0):
        """create a Circle object
        Args:
            radius (int or float): the radius of this circle
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """get this circle's area
        Returns:
            float: this circle's area
        """
        return self.__radius ** 2 * math.pi

    def circunference(self):
        """get this circle's circunference
        Returns:
            float: this circle's circunference
        """
        return 2 * math.pi * self.__radius