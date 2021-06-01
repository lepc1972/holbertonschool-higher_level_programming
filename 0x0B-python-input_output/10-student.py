#!/usr/bin/python3
'''
    Defines a student class
'''


class Student:
    '''
        Defines a student class like a dictionary
    '''
    def __init__(self, first_name, last_name, age):
        '''
            function that Initialize instance variables
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''
            give us the dict representation of the class
        '''
        dict = {}
        if type(attrs) == list:
            for i in attrs:
                if type(i) != str:
                        dict = self.__dict__
                        break
                try:
                    dict[i] = getattr(self, i)
                except:
                    pass
        else:
            dict = self.__dict__
        return (dict)
