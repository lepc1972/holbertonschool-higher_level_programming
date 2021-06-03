#!/usr/bin/python3
"""Module for Rectangle class that includes rectangle area"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class Rectangle that inherits from 'BaseGeometry'"""
    def __init__(self, width, height):
        """private attributes and validate they are ints"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """this Method return area of rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """this Method print Rectangle"""
        return ("[Rectangle] {:d}/{:d}".format(self.__width, self.__height))
