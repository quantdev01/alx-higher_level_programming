#!/usr/bin/python3

def print_last_digit(number):
    temp = 0
    if (number < 0):
        temp = -1 * number % 10
        number = temp
        last_digit = temp
    else:
        last_digit = number % 10

    return last_digit
