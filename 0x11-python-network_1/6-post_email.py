#!/usr/bin/python3
'''Script display mail body response'''
import requests
import sys

if __name__ == "__main__":
    web = sys.argv[1]
    mail = {'email': sys.argv[2]}
    request = requests.post(web, data=mail)
    print(request.text)
