#!/usr/bin/python3
"""This module creates class Rectangle"""


from models.base import Base


class Rectangle(Base):
    """Creation of class Rectangle that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """init Rectangle class"""
        super().__init__(id)
        if type(width) is not int:
            raise TypeError('width must be an integer')
        if type(height) is not int:
            raise TypeError('height must be an integer')
        if type(x) is not int:
            raise TypeError('x must be an integer')
        if type(y) is not int:
            raise TypeError('y must be an integer')
        if width <= 0:
            raise ValueError('width must be > 0')
        if height <= 0:
            raise ValueError('height must be > 0')
        if x < 0:
            raise ValueError('x must be >= 0')
        if y < 0:
            raise ValueError('y must be >= 0')
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """priv attribute getter for width"""
        return (self.__width)

    @property
    def height(self):
        """priv attribute getter for height"""
        return (self.__height)

    @property
    def x(self):
        """priv attribute getter for x"""
        return (self.__x)

    @property
    def y(self):
        """priv attribute getter for y"""
        return (self.__y)

    @width.setter
    def width(self, width):
        """width setter"""
        if width <= 0:
            raise ValueError('width must be > 0')
        if type(width) is not int:
            raise TypeError('width must be an integer')
        self.__width = width

    @height.setter
    def height(self, height):
        """height setter"""
        if height <= 0:
            raise ValueError('height must be > 0')
        if type(height) is not int:
            raise TypeError('height must be an integer')
        self.__height = height

    @x.setter
    def x(self, x):
        """x setter"""
        if type(x) is not int:
            raise TypeError('x must be an integer')
        if x < 0:
            raise ValueError('x must be >= 0')
        self.__x = x

    @y.setter
    def y(self, y):
        """y setter"""
        if y <= 0:
            raise ValueError('y must be > 0')
        if type(y) is not int:
            raise TypeError('y must be an integer')
        self.__y = y

    def area(self):
        """function that give us the rectangle area"""
        return (self.__width * self.__height)

    def display(self):
        """method that display a rectangle with # character"""
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(' ' * self.__x + '#' * self.__width)

    def __str__(self):
        """Overrides __str__ method returns a new rectangle"""
        return ('[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}'.format(
            self.id, self.x, self.y, self.__width, self.__height))

    def update(self, *args):
        """method that assign an argument to each attribute"""
        attributes_list = ["id", "width", "height", "x", "y"]

        if args:
            for i in range(len(args)):
                setattr(self, attributes_list[i], args[i])
