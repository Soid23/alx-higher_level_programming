#!/usr/bin/python3
'''Write a class, and add a special method "to_json"'''


class Student:
    '''Defines a class to hold info of students'''
    def __init__(self, first_name, last_name, age):
        '''Initialize variables on object creation'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''retrieves a dictionary representation of a Student instance'''
        if (isinstance(attrs, list) and
                all(type(elem) == str for elem in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        '''replaces all attributes of the Student instance'''
        for key, value in json.items():
            setattr(self, key, value)
