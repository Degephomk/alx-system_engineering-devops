#!/usr/bin/python3
"""
Function that queries the Reddit API and prints the titles of the first 10
hot posts listed for a given subreddit. If an invalid subreddit is given,
the function should print None.
"""

import requests


def top_ten(subreddit):
    """
    Function that queries the Reddit API and prints the titles of the first 10
    hot posts listed for a given subreddit.
    - If not a valid subreddit, print None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'Custom'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        for post in data['data']['children']:
            print(post['data']['title'])
    else:
        print(None)

