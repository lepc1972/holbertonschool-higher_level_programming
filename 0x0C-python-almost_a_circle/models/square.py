#!/usr/bin/python3
"""class square module"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """square class that inherits from Rectangle class"""
    def __init__(self, size, x=0, y=0, id=None):
        """init square class"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''
        Setting str representation
        '''
        return '[Square] ({}) {}/{} - {}'\
            .format(self.id, self.x, self.y, self.width)

    '''Getter'''
    @property
    def size(self):
        return self.width

    '''Setter'''
    @size.setter
    def size(self, value):
        self.width = value
        self.height = value