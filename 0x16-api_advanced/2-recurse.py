#!/usr/bin/python3
"""returns a list containing the titles of all hot articles
    of all hot articles for a given subreddit"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """recursive function that queries the Reddit API"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}
    params = {'after': after}
    response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False)

    if response.status_code == 404:
        return None
    for post in response.json().get("data").get("children"):
        hot_list.append(post.get("data").get("title"))

    after = response.json().get("data").get("after")
    if after is not None:
        return recurse(subreddit, hot_list, after)
    return hot_list
