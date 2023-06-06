#!/usr/bin/python3
def fizzbuzz():
    """Prints the numbers from 1 to 100 separated by a space.
        For multiples of three print Fizz instead of the number
            and for multiples of five print Buzz.
        For numbers which are multiples of both three and five print FizzBuzz.
        Each element should be followed by a space.
        You are not allowed to import any module."""
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            number = 'FizzBuzz'
        elif number % 3 == 0:
            number = 'Fizz'
        elif number % 5 == 0:
            number = 'Buzz'
        print(number, '', sep=' ', end='')
