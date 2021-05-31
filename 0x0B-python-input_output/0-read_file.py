#!/usr/bin/python3
"""Module for read the file with read_file method"""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints to stdout"""
    with open(filename, 'r', encoding='utf-8') as file:
        read_data = file.read()
        print(read_data, end='')
