#!/usr/bin/python3
'''
    Module that defines a student class
'''


class Student:
    '''
        Defines a student class
    '''
    def __init__(self, first_name, last_name, age):
        '''
            constructor method for Initializing instance variables
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''
            give us  the dictionary representation of the class
        '''
        return self.__dict__
