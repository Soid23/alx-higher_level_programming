#!/usr/bin/python3
""" function that writes an Object to a text file,"""
import jnson


def save_to_json_file(my_obj, filename):
    """ JSON representation"""
    with open(filename, "w") as f:
        return json.dump(my_obj, f)
