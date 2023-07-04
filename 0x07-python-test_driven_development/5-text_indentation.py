#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""This module contains a function -text_indentation
that prints a text with 2 new lines
after each of these characters: '., ? and :'
"""


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    # There should be no space at the beginning or at the end of each printed line
    for letter in text:
        if letter in [".", ":", "?"]:
            print(letter, "\n")
        else:
            print(letter, end="")
    """sentences = []
    for splitt in text.split("."):
        for spli in splitt.split(":"):
            for spl in spli.split("?"):
                sentences.append(spl)
    for sentence in sentences:
        print(sentence, '\n')
    print(sentences)"""
