#!/usr/bin/python3
"""This module creates class Rectangle"""


from models.base import Base


class Rectangle(Base):
    """Creation of class Rectangle that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """init Rectangle class"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
