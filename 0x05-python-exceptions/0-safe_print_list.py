#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    mylen = 0
    for j in range(0, x):
        try:
            print("{}".format(my_list[j]), end="")
            mylen += 1
        except IndexError:
            break
    print()
    return mylen
