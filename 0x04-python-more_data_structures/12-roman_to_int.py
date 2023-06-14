#!/usr/bin/python3


def roman_to_int(roman_string):
    '''
    Converts a Roman numeral to an integer.
        assume number is between 1 to 3999.
        must return an integer or 0 - if roman_sting is not a string or None
    '''
    dictionary = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
        }
    result = 0
    if not isinstance(roman_string, str) or roman_string is None:
        return result
    for position, numeral in enumerate(roman_string):
        numeral_value = dictionary[numeral]
        string_size = len(roman_string)
        next_position = position + 1
        if next_position < string_size:
            if dictionary[roman_string[next_position]] > numeral_value:
                result -= numeral_value
            else:
                result += numeral_value
        else:
            result += numeral_value
    return result
