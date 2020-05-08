#!/usr/bin/python3
"""Write a function that queries the Reddit API
"""
import requests


def number_of_subscribers(subreddit):
    user = {'User-agent': 'my-app/0.0.1'}
    fetch = requests.get('http://www.reddit.com/r/{}/about.json'
                         .format(subreddit), headers=user)
    try:
        fetch = fetch.json().get('data')
        for key, values in fetch.items():
            if key == 'subscribers':
                return(values)
    except:
        return(0)
