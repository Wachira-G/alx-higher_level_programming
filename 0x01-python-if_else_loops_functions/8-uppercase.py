#!/usr/bin/python3
def uppercase(str):
    """Prints a string in uppercase followed by a new line."""
    for character in str:
        if ord(character) in range(97, 123):
            character = chr(ord(character) - 32)
        print(character, end='')
    print()
