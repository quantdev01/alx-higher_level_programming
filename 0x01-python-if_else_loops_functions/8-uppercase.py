#!/usr/bin/python3

def uppercase(str):
    for i in range(len(str)):
        char = str[i]
        # Check if the character is lowercase
        if (ord(char) >= 97 and ord(char) <= 122):
            to_upper = ord(char) - 32
            char = chr(to_upper)
        print('{}'.format(char), end='')
    print()
