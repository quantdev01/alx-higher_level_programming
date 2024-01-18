#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    lenstr = len(sys.argv)

    if (lenstr < 4):
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])
    s = 0
    if (operator == '+'):
        s = add(a, b)
    elif (operator == '-'):
        s = sub(a, b)
    elif (operator == '*'):
        s = mul(a, b)
    elif (operator == '/'):
        s = div(a, b)
    else:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)
    print(f'{a} {operator} {b} = {s}')
    exit(0)
