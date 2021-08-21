#!/usr/bin/python3
"""send a letter with a post method"""
import sys
import requests

if __name__ == '__main__':
    web = 'http://0.0.0.0:5000/search_user'
    try:
        r = requests.post(web, data={'q': sys.argv[1]})
    except IndexError:
        r = requests.post(web, data={'q': ""})
    try:
        r = r.json()
        if not r:
            print('No result')
        else:
            print('[{}] {}'.format(r.get('id'), r.get('name')))
    except ValueError:
        print('Not a valid JSON')
