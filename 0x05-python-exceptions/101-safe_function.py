#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    '''Executes a function safely'''
    try:
        result = fct(*args)
        return result
    except Exception as error:
        error_message = str(error)
        print("Exception: {}".format(error_message), file=sys.stderr)
        return None
