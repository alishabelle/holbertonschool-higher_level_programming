#!/usr/bin/python3
""" documentation module - improve geometry """


class BaseGeometry:
    """ class that raises an exception """
    def area(self):
        raise Exception("area() is not implemented")

    """ validates int value """
    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """ rectangle class that inherits basegeometry class """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
