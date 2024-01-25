#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    copy_dico = {}

    for k, v in a_dictionary.items():
        copy_dico[k] = v * 2
    return copy_dico
