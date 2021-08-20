#!/usr/bin/python3
"""scrip that takes 2 args, url n mail, so give us response body"""
import urllib.request
import urllib.parse
from sys import argv


if __name__ == '__main__':
    web = argv[1]
    mail = argv[2]

    data = {"email": mail}
    val = urllib.parse.urlencode(data)
    val = val.encode("ascii")
    req = urllib.request.Request(web, val)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode("utf-8"))
