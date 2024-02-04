#!/usr/bin/python3

def max_integer(my_list=[]):
    n = 0
    if my_list is None:
        return None

    j = 0

    for i in range(0, len(my_list)):
        if i == len(my_list) - 1:
            break
        if (n > my_list[i+1]):
            if (j < n):
                j = n
        n = my_list[i]
    return j
