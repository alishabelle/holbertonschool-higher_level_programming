#!/usr/bin/python3
""" write first class base """


class Base:
    """ creating base class """

    __nb_objects = 0

    def __init__(self, id=None):
        """  instantiation of id """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
