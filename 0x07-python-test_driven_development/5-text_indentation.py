#!/usr/bin/python3
"""Module for text_indentation method"""


def text_indentation(text):
    """Function that prints text with 2 new lines after . ? and :"""
    if type(text) is not str:
        raise TypeError('text must be a string')

    stri = ''
    for x in text:
        if x in '.?:':
            stri = stri + x
            print(stri.strip(' '))
            print()
            stri = ''
        else:
            stri = stri + x
    print(stri.strip(' '), end='')
