#!/usr/bin/python3
"""
Function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0
"""
import requests

def get_subreddit_subscribers(subreddit):
    """
    Get the number of subscribers for a subreddit from the Reddit API.
    Returns 0 if the subreddit is not found or there was an error.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Custom"}
    response = requests.get(url, headers=headers)
    
    if response.ok:
        data = response.json().get("data")
        if data:
            return data.get("subscribers", 0)
    
    return 0
