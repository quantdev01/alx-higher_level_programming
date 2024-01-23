#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    len_list = len(my_list)
    my_list.reverse()
    j = 0

    while (j < len_list):
        print("{}".format(my_list[j]))
        j += 1
