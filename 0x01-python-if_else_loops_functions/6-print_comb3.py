#!/usr/bin/python3

for i in range(0, 10):
    for j in range(1, 10):
        if i >= 1:
            j = j + i
        if (i <= 7 and j <= 9):
            print('{}{}, '.format(i, j), end='')
        if (i == 8 and j == 9):
            print('{}{}'.format(i, j))
