#!/usr/bin/python3
def print_last_digit(number):
    """Prints the last digit of a number."""
    last_digit = int(str(number)[-1])
    if last_digit < 0:
        last_digit *= -1
    print(last_digit, end='')
    return last_digit
