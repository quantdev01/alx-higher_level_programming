#!/usr/bin/python3

def max_integer(my_list=[]):
    n = 0
    j = 0
    if len(my_list) == 0:
        return None


    for i in range(0, len(my_list) - 1):
        if i == len(my_list) - 1:
            break
        if (n > my_list[i+1]):
            if (j < n):
                j = n
        n = my_list[i]
    return j
