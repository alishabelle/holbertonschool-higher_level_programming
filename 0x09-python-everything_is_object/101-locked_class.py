#!/usr/bin/python3
""" creating a locked class """


class LockedClass:
    """ allows no other new attributes to be created """
    __slots__ = 'first_name'
