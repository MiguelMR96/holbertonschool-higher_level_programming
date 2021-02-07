#!/usr/bin/python3
""" script that takes in a URL and an email,
sends a POST request
"""
import urllib.request
from sys import argv

if __name__ == "__main__":
    email = {}
    email["email"] = argv[2]
    value = urllib.parse.urlencode(email)
    value = value.encode("ascii")
    with urllib.request.urlopen(argv[1], value) as response:
        req = response.read()
        print(req.decode("utf-8"))
