#!/usr/bin/python3
'''Description'''


BaseGeometry = __import__('7-base_geometry').


class Rectangle(BaseGeometry):
    '''Inheritance of BaseGeometry'''

    def __init__(self, width, height):
        '''Method of instance'''

        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height

    def area(self):
        '''This method calculates the area of the rectangle'''
        return self.__width * self.__height

    def __str__(self):
        '''Informal representation of the rectangle'''
        return '[Rectangle] {}/{}'.format(self.__width, self.__height)
