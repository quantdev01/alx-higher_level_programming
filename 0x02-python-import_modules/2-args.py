#!/usr/bin/python3

import sys

if (len(sys.argv) == 1):
    print('0 arguments.')
else:
    print(f'{len(sys.argv) -1} argument:')
    for i in range(1, len(sys.argv)):
        print(f'{i}: {sys.argv[i]}')
