#!/usr/bin/python3
""" script that takes in a URL, sends a request to the URL
"""
import urllib.request
from sys import argv
from urllib.error import HTTPError

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(argv[1]) as response:
            req = response.read()
            print(req.decode("utf-8"))
    except HTTPError as e:
        print('Error code:', e.code)
