#!/usr/bin/python3
"""
python3 -c 'print(__import__("my_module").__doc__)'
"""


def add_integer(a, b=98):
    """
    python3 -c 'print(__import__("my_module").my_function.__doc__)'
    """

    if isinstance(a, bool) and isinstance(b, str):
        raise TypeError("a and b must be integers")
    if isinstance(a, str) and isinstance(b, bool):
        raise TypeError("a and b must be integers")
    if isinstance(a, bool) and isinstance(b, bool):
        raise TypeError("a and b must be integers")
    if isinstance(a, bool):
        raise TypeError("a must be an integer")
    if isinstance(b, bool):
        raise TypeError("b must be an integer")
    if isinstance(a, str) and isinstance(b, str) or a is None and b is None:
        raise TypeError("a and b must be integers")
    if isinstance(a, str) or a is None:
        raise TypeError("a must be an integer")
    if isinstance(b, str) or b is None:
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)
    return a + b
