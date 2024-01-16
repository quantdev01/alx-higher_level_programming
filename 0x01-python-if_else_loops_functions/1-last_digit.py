#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

temp = 0

if number < 0:
    temp = (-1 * number) % 10
    last_digit = temp*-1
else:
    last_digit = number % 10

if last_digit > 5 and number > 0:
    print(f'Last digit of {number:d} is {last_digit:d} and is greater than 5')
elif last_digit == 0:
    print(f'Last digit of {number:d} is {last_digit:d} and is 0')
else:
    print(f'Last digit of {number:d} is\
 {last_digit:d} and is less than 6 and not 0')
