#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = int(str(number)[-1])

if last_digit > 5:
    string = 'and is greater than 5'
elif last_digit == 0:
    string = 'and is 0'
else:
    string = 'and is less than 6 and not 0'

print(f'Last digit of {number:d} is {last_digit:d} {string}')
