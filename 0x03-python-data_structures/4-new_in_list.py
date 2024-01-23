#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    len_list = len(my_list)
    if idx < 0:
        return my_list
    if idx >= len(my_list):
        return my_list

    new_list = []
    #inserting in the new list the old list values
    for i in range(len_list):
        new_list.append(my_list[i])
    #removing and replacing the element
    new_list.pop(idx)
    new_list.insert(idx, element)
    return new_list #returning the list
