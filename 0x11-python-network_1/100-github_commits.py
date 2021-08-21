#!/usr/bin/python3
"""repo rails user rails 10 commits"""
import requests
import sys


if __name__ == '__main__':
    repo = sys.argv[1]
    owner = sys.argv[2]
    web = 'https://api.github.com/repos/{}/{}/commits'.format(owner,
                                                              repo)
    request = requests.get(web)
    json_response = request.json()
    for i in json_response[:10]:
        print('{}: {}'.format(i.get('sha'),
                              i.get('commit').get('author').get('name')))
