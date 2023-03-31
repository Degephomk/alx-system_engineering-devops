#!/usr/bin/python3
import requests


def count_words(subreddit, word_list, count_dict=None):
    """
    Recursive function that queries the Reddit API, parses the title of all hot
    articles, and prints a sorted count of given keywords.
    """
    if count_dict is None:
        count_dict = {}
    req = requests.get(
        f"https://www.reddit.com/r/{subreddit}/hot.json",
        headers={"User-Agent": "Custom"},
        params={"limit": 100},
    )
    if req.status_code == 200:
        data = req.json()["data"]
        children = data["children"]
        for child in children:
            title = child["data"]["title"].lower()
            for word in word_list:
                if word.lower() in title and not title[title.index(word.lower())-1].isalpha() and not title[title.index(word.lower())+len(word)].isalpha():
                    if word.lower() in count_dict:
                        count_dict[word.lower()] += 1
                    else:
                        count_dict[word.lower()] = 1
        if data["after"]:
            return count_words(subreddit, word_list, count_dict=count_dict)
        else:
            # sort the count_dict by count and alphabetically
            sorted_count = sorted(
                count_dict.items(),
                key=lambda x: (-x[1], x[0])
            )
            # print the sorted count
            for word, count in sorted_count:
                print(f"{word}: {count}")
    else:
        print(None)

