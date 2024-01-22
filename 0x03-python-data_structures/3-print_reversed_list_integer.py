#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    len_list = len(my_list)
    i = len_list
    my_list.reverse()
    j = 0

    for j in range(i):
        print("{}".format(my_list[j]))
