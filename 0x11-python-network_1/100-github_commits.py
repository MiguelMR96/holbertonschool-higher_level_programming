#!/usr/bin/python3
""" Script that takes 2 arguments
"""
import requests
import sys


if __name__ == '__main__':
    owner = sys.argv[2]
    repository = sys.argv[1]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner,
                                                              repository)
    request = requests.get(url)
    json_response = request.json()
    for i in json_response[:10]:
        print('{}: {}'.format(i.get('sha'),
                              i.get('commit').get('author').get('name')))
