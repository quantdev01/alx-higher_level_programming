#!/usr/bin/python3
"""
Module read text file and print it to stdout
"""


def read_file(filename=""):
    """
    function to read the file and print it out
    """
    with open(filename, encoding="utf-8") as file:
        for line in file:
            print(line.rstrip())
