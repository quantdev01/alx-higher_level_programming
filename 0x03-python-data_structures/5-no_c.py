#!/usr/bin/python3

def no_c(my_string):
    ln = len(my_string)
    lists = []

    # putting the my_string char in a list
    # without the c
    for i in range(ln):
        if (my_string[i] == 'c' or my_string[i] == 'C'):
            continue
        lists.append(my_string[i])
    # returning the joined string
    return ''.join(lists)
