#!/usr/bin/python3

import calculator_1 as calc

if __name__ == "__main__":
    a = 10
    b = 5

    print('10 + 5 = {}'.format(calc.add(a, b)))
    print('10 - 5 = {}'.format(calc.sub(a, b)))
    print('10 * 5 = {}'.format(calc.mul(a, b)))
    print('10 / 5 = {}'.format(calc.div(a, b)))
