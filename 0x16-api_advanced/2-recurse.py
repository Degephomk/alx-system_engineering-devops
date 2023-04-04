#!/usr/bin/python3
"""Queries and returns a list"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Returns list of titles of hot articles"""
    try:
        r = requests.get("https://www.reddit.com/r/{}/hot.json".
                         format(subreddit),
                         headers={"User-Agent": "custom"},
                         params={"after": after},
                         allow_redirects=False).json()
    except:
        return None

    if ("data" in r and "children" in r.get("data")):
        for i in r.get("data").get("children"):
            hot_list.append(i.get("data").get("title"))
        if "after" in r.get("data") and r.get("data").get("after"):
            return recurse(subreddit, hot_list,
                           r.get("data").get("after"))
        else:
            return hot_list
    else:
        return None
