#!/usr/bin/python3
for char in range(122, 96, -1):
    print('{}'.format(chr(char - (char % 2) * 32)), end='')
