#!/usr/bin/python3
"""Reddit API and prints the titles of the first 10"""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts."""
    r = requests.get("https://reddit.com/r/{}.json?sort=hot&limit=10".
                     format(subreddit), headers={"User-Agent": "custom"})

    if (r.status_code == 200):
        for item in r.json().get("data").get("children"):
            print(item.get("data").get("title"))
    else:
        print("None")
