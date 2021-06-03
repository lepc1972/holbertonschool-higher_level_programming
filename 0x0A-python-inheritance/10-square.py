#!/usr/bin/python3
"""
Implementing a new class called Rectangle
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    '''
    the class Square
    '''
    def __init__(self, size):
        '''
        Square class inheriting Rectangle class attributes
        '''
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return Rectangle.area(self)
