#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    lenstr = len(sys.argv)
    s = 0

    if (lenstr) == 0:
        print(s)
    else:
        for i in range(1, lenstr):
            s = s + int(sys.argv[i])
    print(s)
