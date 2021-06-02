#!/usr/bin/python3
"""Module for MyList class that sort a list"""


class MyList(list):
    """Inherit from list"""
    def print_sorted(self):
        """Method to print sorted list"""
        print(sorted(self))
