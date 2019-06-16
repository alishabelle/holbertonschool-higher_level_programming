#!/usr/bin/python3
class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        a = self.__dict__
        if attrs is None:
            return(a)
        new_jawn = {}
        for k, val, in a.items():
            if k in attrs:
                new_jawn[k] = val
        return(new_jawn)

    def reload_from_json(self, json):
        for k, val in json.items():
            setattr(self, k, val)
