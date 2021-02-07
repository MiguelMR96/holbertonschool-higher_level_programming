#!/usr/bin/python3
""" Script that takes in a URL and an email address,
sends a POST request to the passed URL with the email as a parameter
"""
import requests
import sys

if __name__ == "__main__":
    email = {}
    email["email"] = sys.argv[2]
    req = requests.post(sys.argv[1], email)
    print(req.content.decode("utf-8"))
