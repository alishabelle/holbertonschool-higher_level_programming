#!/usr/bin/python3
class Square:
    """Defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        if not (len(position) > 2 or isinstance(position, tuple)):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (not isinstance(position[0], int) or
                not isinstance(position[1], int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (position[0] < 0 or position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not (len(value) > 2 or isinstance(value, tuple)):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not (isinstance(value[0], int) or not isinstance(value[1], int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        if self.__size == 0:
            print()
            return
        for index in range(self.__position[1]):
            print()
        for idx in range(self.__size):
            print("{}{}".format(" " * self.__position[0], "#" * self.__size))
