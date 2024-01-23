#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    len_list = len(my_list)
    if idx < 0:
        return my_list
    if idx >= len(my_list):
        return my_list

    print("Print in BEFORE function")
    temp_list = my_list
    print(my_list)
    my_new_list = temp_list
    my_new_list.pop(idx)
    my_new_list.insert(idx, element)


    print("Print in the function")

    print(my_list)
    
    return my_new_list
