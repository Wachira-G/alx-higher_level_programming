#!/usr/bin/python3
for letter in range(97, 123):
    if letter in [ord('q'), ord('e')]:
        continue
    else:
        print('{}'.format(chr(letter)), end='')
