#!/usr/bin/python3
""" This module contains a function that queries
    RedditAPI for subreddits """

import json
import requests
import sys


def number_of_subscribers(subreddit):
    """ Returns the number of subscribers for a given subreddit """
    user_agent = 'Mozilla/5.0'
    headers = {
        'User-Agent': user_agent
    }

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    subs = response.json()
    if 'data' not in subs:
        return 0
    if 'subscribers' not in subs.get('data'):
        return 0
    return response.json()['data']['subscribers']
