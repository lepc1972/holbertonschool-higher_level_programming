#!/usr/bin/python3
"""Module to create __init__ method and .__size"""


class Square:
    """Square with private instance attribute"""
    def __init__(self, size):
        """Initialize data"""
        self.__size = size
        """Private instantiation of size"""
