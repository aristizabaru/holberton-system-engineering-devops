"""module 0-subs.py

Queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit."""

    if subreddit is not None and type(subreddit) is str:
        HEADERS = {'User-Agent': 'Python:Holberton School '
                   'API project:v1.0.0 (by /u/aristizabaru)'}
        END_POINT = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)

        response = requests.get(END_POINT, headers=HEADERS)
        if response.status_code == requests.codes.ok:
            return response.json().get('data').get('subscribers')
    return 0
