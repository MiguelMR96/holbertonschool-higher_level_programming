#!/usr/bin/python3
""" Script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
from sys import argv

if __name__ == "__main__":
    letter = ""
    if len(argv) > 1 and argv[1].isalpha():
        letter = argv[1]
        req = requests.post('http://0.0.0.0:5000/search_user',
                            data={'q': letter})
        json_format = req.json()
        print("[{}] {}".format(json_format.get('id'), json_format.get('name')))
    else:
        print("No result")
