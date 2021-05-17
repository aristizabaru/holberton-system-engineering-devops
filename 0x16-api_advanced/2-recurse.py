#!/usr/bin/python3
"""module 1-top_ten.py

Returns a list containing the titles of all hot
articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], next=True, after=''):
    """Returns a list containing the titles of all hot 
    articles for a given subreddit."""

    # base case
    if next:
        if subreddit is not None and type(subreddit) is str:
            LIMIT = 100
            HEADERS = {'User-Agent': 'Python:Holberton School '
                       'API project:v1.0.0 (by /u/aristizabaru)'}
            END_POINT = 'https://www.reddit.com/r/{}/hot.json'\
                        .format(subreddit)

            response = requests.get(
                END_POINT,
                headers=HEADERS,
                params={'limit': LIMIT, 'after': after})

            if response.status_code == requests.codes.ok:
                nodes = response.json()['data']['children']
                node_list = response.json()['data']

                if len(nodes) is not None and nodes[0]['kind'] == 't3':
                    for item in nodes:
                        hot_list.append(item['data']['title'])
                        # print(item['data']['title'])
                    if node_list['after']:
                        recurse(subreddit, hot_list, True, node_list['after'])
                    else:
                        # print('*'*50)
                        # print('Node "After" is equal to: {}'.format(
                        #     node_list['after']))
                        # print('*'*50)
                        recurse(subreddit, hot_list, False, node_list['after'])
                else:
                    return None
            else:
                return None
        else:
            return None
    return hot_list
