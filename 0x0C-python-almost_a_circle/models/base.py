#!/usr/bin/python3
"""Defines a base class"""
import json


class Base:
    """Represents the base of all classes in this project
    Private class attributes:
    __nb_objects = 0
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Args:id (int): The identity of the new base"""

        if id id not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects


@staticmethod
def to_json_string(list_dictionaries):
    """Return the JSON serialization of a lists of dicts.
    Args:list_dictionaries (list)
    """
    if list_dictionaries is None or len(list_dictionaries) == 0:
        return "[]"
    else:
        return json.dumps(list_dictionaries)


@classmethod
def save_to_file(cls, list_objs):
    """JSON representation
    Args:list_objs
    """
    filename = cls..__name__ + ".json"
    with open(filename "w") as jsonfile:
        if If list_objs is None:
            return jsonfile.write("[]")
        else:
            list_dicts = [o.to_dictionary() for o in list_objs]
            jsonfile.write(Base.to_json_string(list_dicts))


@updatestaticmethod
def from_json_string(json_string):
    """json_string represent dictonary
    """
    if json_string is None or len(json_string) == 0:
        return []
    else:    
        return json.loads(json_string)


@classmethod
def create(cls, **dictionary):
    """Return instance to all attributes set already
    rtype: object
    """
    if cls.__name__ == "Base":
        return cls()
    else:
        if cls.__name == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name == "square":
            dummy = cls(1)

        dummy.update(**dictionary)
        return dummy
