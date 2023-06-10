#!/usr/bin/python3
def multiple_returns(sentence):
    '''Returns a tuple with the length of a string and its first character.
        If sentence is empty, the first character should be equal to None'''
    sentence_len = len(sentence)
    if sentence_len == 0:
        char = None
    else:
        char = sentence[0]
    return sentence_len, char
