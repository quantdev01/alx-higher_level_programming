#!/usr/bin/python3

def uppercase(str):
    for i in range(len(str)):
        if (i == len(str)-1):
            x = str[i]
            if (ord(x) >= 32 and ord(x) <= 96):
                to_lower = ord(x) + 32
                x = chr(to_lower)
            if (x == ''):
                x = ''
            to_upper = ord(x) - 32
            x = chr(to_upper)
            print('{}'.format(x))
        else:
            y = str[i]
            if (ord(y) >= 32 and ord(y) <= 96):
                to_lower = ord(y) + 32
                y = chr(to_lower)
            to_upper = ord(y) - 32
            y = chr(to_upper)
            print('{}'.format(y), end='')
