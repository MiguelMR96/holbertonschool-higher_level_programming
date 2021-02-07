#!/usr/bin/python3
""" Script that fetches https://intranet.hbtn.io/status
"""
import requests

if __name__ == "__main__":
    req = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: ", end="")
    print(type(str(req)))
    print("\t- content: ", end="")
    print(req.text)
