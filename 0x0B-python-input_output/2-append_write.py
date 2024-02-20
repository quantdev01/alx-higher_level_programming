#!/usr/bin/python3
"""
Module that append into a file
"""


def append_write(filename="", text=""):
    """must append the text as input and create a file
    Args:
        filename - path to the file
        text - contains the text to append
    Return:
        return - the text char number
    """
    with open(filename, mode='a', encoding='utf-8') as file:
        return file.write(text)
