#!/usr/bin/python3

import sys

if __name__ == ("__main__"):
    lenstr = len(sys.argv)

    if (lenstr == 1):
        print('0 arguments.')
    else:
        if(lenstr <= 2):
            print(f'{lenstr -1} argument:')
        else:
            print(f'{lenstr -1} arguments:')
        for i in range(1, len(sys.argv)):
            print(f'{i}: {sys.argv[i]}')
