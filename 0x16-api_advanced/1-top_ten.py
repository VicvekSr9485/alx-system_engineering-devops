#!/usr/bin/python3
""" This module queries the Reddit API and prints the
    titles of the first 10 hot posts
        listed for a given subreddit
"""

import json
import requests
import sys


def top_ten(subreddit):
    """ Returns first 10 hot posts listed for
        a given subreddit """
    user_agent = 'Mozilla/5.0'
    headers = {
        'User-Agent': user_agent
    }

    params = {
        'limit': 10
    }
    url = "https://www.reddit.com/r/" + subreddit + "/hot.json"

    response = requests.get(url,
                            headers=headers,
                            params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return
    dic = response.json()
    hot_posts = dic['data']['children']
    if len(hot_posts) is 0:
        print(None)
    else:
        for post in hot_posts:
            print(post['data']['title'])
