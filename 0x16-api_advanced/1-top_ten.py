#!/usr/bin/python3
""" Top 10 hot posts """
import json
import requests
from sys import argv


def top_ten(subreddit):
    try:
        user = {'user-agent': 'my-app/0.0.1'}
        fetch = requests.get('http://www.reddit.com/r/{}/hot.json'
                             .format(subreddit), headers=user_agent)
        data_x = fetch.json()

        for x in range(10):
            print(data_x.get('data').get('children')[x].get('data')['title'])

    except:
        print(None)
