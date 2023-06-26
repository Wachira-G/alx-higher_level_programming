#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    '''prints an integer'''
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError) as error:
        error_message = str(error)
        print("Exception: {}".format(error_message), file=sys.stderr)
        return False
