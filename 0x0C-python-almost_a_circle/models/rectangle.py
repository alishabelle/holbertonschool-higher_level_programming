#!/usr/bin/python3
""" writing rectangle class that inherits base """

from models.base import Base


class Rectangle(Base):
    """ creating rectangle class """

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, value):
        self.__width = value
    if not isinstance(width, int):
        raise TypeError("width must be an integer")
    if width <= 0:
        raise ValueError("width must be > 0")

    @height.setter
    def height(self, value):
        self.__height = value
    if not isinstance(height, int):
        raise TypeError("height must be an integer")
    if height <= 0:
        raise ValueError("height must be > 0")

    @x.setter
    def x(self, value):
        self.__x = value
        if x < 0:
            raise ValueError("x must be >= 0")

    @y.setter
    def y(self, value):
        self.__y = value
        if y < 0:
            raise ValueError("y must be >= 0")

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

