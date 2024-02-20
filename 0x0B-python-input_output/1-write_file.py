#!/usr/bin/python3
"""
Write into file module
"""


def write_file(filename="", text=""):
    """
    function to write into a file and return the number of character
    """
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
