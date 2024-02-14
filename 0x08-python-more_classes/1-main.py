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
print()
print()
print("Normal one")
print("------------------")
my_rectangle = Rectangle(2, 4)
print(my_rectangle.__dict__)

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle.__dict__)
