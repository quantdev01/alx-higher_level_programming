#!/usr/bin/python3

def uniq_add(my_list=[]):
    unique_number = list(set(my_list))
    s = 0

    for i in range(len(unique_number)):
        s = s + unique_number[i]

    return s
