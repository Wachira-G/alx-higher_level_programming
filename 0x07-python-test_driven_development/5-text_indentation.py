#!/usr/bin/python3
"""This module contains a function -text_indentation
that prints a text with 2 new lines
after each of these characters: '., ? and :'
"""


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    add_newline = False

    for letter in text:
        if letter in [".", ":", "?"]:
            result += letter + "\n\n"
            add_newline = True
        elif letter == " " and add_newline:
            continue
        else:
            result += letter
            add_newline = False
    print(result.strip(" "))

    """sentences = []
    for splitt in text.split("."):
        for spli in splitt.split(":"):
            for spl in spli.split("?"):
                sentences.append(spl)
    for sentence in sentences:
        print(sentence, '\n')
    print(sentences)"""
