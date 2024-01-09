#!/usr/bin/python3
"""appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """appends at end of text line"""
    with open(filename, "a", encodimg"utf-8") as f:
        return f.write(text)
