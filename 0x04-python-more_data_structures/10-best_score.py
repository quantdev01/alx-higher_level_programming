#!/usr/bin/python3

def best_score(a_dictionary):
    i = 0
    v = ''
    if (a_dictionary is None or a_dictionary == {}):
        return None

    for key, value in a_dictionary.items():
        if i == 0:
            i = value
            v = key

        if (i > value):
            continue
        else:
            i = value
            v = key

        i += 1

    return v
