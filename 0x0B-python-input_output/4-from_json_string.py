#!/usr/bin/python3
"""returns an object (Python data structure) rep by json"""
import json


def from_json_string(my_str):
    """returns an object (json)"""
    return json.loads(my_str)
