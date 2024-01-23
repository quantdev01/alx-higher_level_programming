#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    ln_a = len(tuple_a)
    ln_b = len(tuple_b)
    if (ln_a > 2 and ln_b < 2):
        return (tuple_a[0] + tuple_b[0], tuple_a[1] + 0)
    if (ln_b < 2):
        return (tuple_a[0] + 0, tuple_a[1] + 0)

    if (ln_a >= 2 and ln_b >= 2):
        return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
