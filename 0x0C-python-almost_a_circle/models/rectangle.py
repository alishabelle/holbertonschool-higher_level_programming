#!/usr/bin/python3
""" writing rectangle class that inherits base """

from models.base import Base


class Rectangle(Base):
    """ creating rectangle class """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ returns the value of width """
        return self.__width

    @property
    def height(self):
        """ returns the value of height """
        return self.__height

    @property
    def x(self):
        """ returns the value of x """
        return self.__x

    @property
    def y(self):
        """ returns the value of y """
        return self.__y

    @width.setter
    def width(self, value):
        """ sets value of width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """ set value of height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """ set value of x """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """ sets value of y """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ creating area of rect """
        return (self.__width * self.__height)

    def display(self):
        """ creating display of rect """
        for i in range(self.y):
            print('' * (self.y))
        for i in range(self.__height):
            print(' ' * self.x + "#" * self.width)

    def __str__(self):
        """ prints string of rect """
        return ("[Rectangle] ({}) {}/{} - {}/{}".
                format(self.id, self.x, self.y,
                       self.width, self.height))

    def update(self, *args, **kwargs):
        """ update some file """
        a = 0
        for idx in args:
            a += 1
            if a == 1:
                self.id = idx
            if a == 2:
                self.width = idx
            if a == 3:
                self.height = idx
            if a == 4:
                self.x = idx
            if a == 5:
                self.y = idx
        if not args:
            for key, value in kwargs.items():
                if key == 'id':
                    setattr(self, key, value)
                if key == 'width':
                    setattr(self, key, value)
                if key == 'height':
                    setattr(self, key, value)
                if key == 'x':
                    setattr(self, key, value)
                if key == 'y':
                    setattr(self, key, value)

    def to_dictionary(self):
        """ prints dict of object """
        jawn = {'id': self.id, 'width': self.width, 'height': self.height,
                'x': self.x, 'y': self.y}
        return jawn
