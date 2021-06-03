#!/usr/bin/python3
"""Module for Rectangle class that inherits from base-geometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class Rectangle inherits from '7-BaseGeometry'"""
    def __init__(self, width, height):
        """Instantiation  private attributes and validate are ints"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
