#!/usr/bin/python3
'''takes url and displays handling errors'''
import requests
import sys


if __name__ == '__main__':
    web = sys.argv[1]
    request = requests.get(web)
    if request.status_code >= 400:
        print('Error code: {}'.format(request.status_code))
    else:
        print(request.text)
