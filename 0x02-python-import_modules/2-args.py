#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    lenstr = len(sys.argv)

    if (lenstr == 1):
        print('0 arguments.'.format())
    else:
        if(lenstr <= 2):
            print('{} argument:'.format(lenstr - 1))
        else:
            print('{} arguments:'.format(lenstr - 1))
        for i in range(1, len(sys.argv)):
            print('{}: {}'.format(i, sys.argv[i]))
