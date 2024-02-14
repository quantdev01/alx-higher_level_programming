#!/usr/bin/python3
"""
My module
"""


def text_indentation(text):
    """
    function
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    for c in range(len(text)):
        if text[c] == '.' or text[c] == '?' or text[c] == ':':
            print()
            print()
        else:
            print(text[c], end="")
