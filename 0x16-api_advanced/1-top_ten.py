#!/usr/bin/python3
"""module 1-top_ten.py

Prints the titles of the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts listed for a given subreddit"""

    if subreddit is not None and type(subreddit) is str:
        LIMIT = 10
        HEADERS = {'User-Agent': 'Python:Holberton School '
                   'API project:v1.0.0 (by /u/aristizabaru)'}
        END_POINT = 'https://www.reddit.com/r/{}/hot.json?limit={}'\
                    .format(subreddit, LIMIT)

        response = requests.get(END_POINT, headers=HEADERS)
        if response.status_code == requests.codes.ok:
            nodes = response.json().get('data').get('children')

            for item in nodes:
                print(item.get('data').get('title'))
        else:
            print(None)
    else:
        print(None)
