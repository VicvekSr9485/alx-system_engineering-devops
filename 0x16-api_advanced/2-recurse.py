#!/usr/bin/python3
""" queries the Reddit API and returns a list
    containing the titles of all hot articles
        for a given subreddit """
    
import json
import requests
import sys


def recurse(subreddit, hot_list=[]):
    """ returns list containing the titles of
        all hot articles for a given subreddit
    """
    user_agent = 'Mozilla/5.0'

    headers = {
        'User-Agent': user_agent
    }

    
