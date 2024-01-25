#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    key = sorted(a_dictionary)
    for i in range(len(key)):
        print(f'{key[i]}: {a_dictionary[key[i]]}')
