#!/usr/bin/python3
Rectangle = __import__('1-rectangle').Rectangle

try:
    my_rectangle = Rectangle(2, "3")
except Exception as e:
    print(e)

try:
    myrectangle = Rectangle("2", 3)
except Exception as e:
    print(e)
