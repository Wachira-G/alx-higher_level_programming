#!/usr/bin/python3
for dig1 in range(0, 8):
    for dig2 in range(0, 10):
        if dig2 <= dig1:
            continue
        else:
            print('{}{}'.format(dig1, dig2), '', sep=', ', end='')
print('{}{}'.format(dig1 + 1, dig2))
