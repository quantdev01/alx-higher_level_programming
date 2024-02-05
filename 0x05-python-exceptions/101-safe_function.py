#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    try:
        fct(args)
    except ZeroDivisionError
    except (NameError, TypeError, ValueError) as element:
        print("Exception: {}".format(element), file=sys.stderr)
