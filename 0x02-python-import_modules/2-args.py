#!/usr/bin/python3
import sys
if __name__ == '__main__':
    argv_len = len(sys.argv)
    args = sys.argv[1:]
    if argv_len == 1:
        print('0 arguments.')
    elif argv_len == 2:
        print('1 argument:')
        print('1: {}'.format(args[0]))
    else:
        print('{} arguments:'.format(len(args)))
        for number, argument in enumerate(args, start=1):
            print('{}: {}'.format(number, argument))
