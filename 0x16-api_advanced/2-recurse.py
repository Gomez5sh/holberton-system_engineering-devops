#!/usr/bin/python3
'''
displays top 10 hot posts
'''
import requests


def recurse(subreddit, hot_list=[], after=None):
    user = {'User-agent': 'greg'}
    fetch = requests.get('http://www.reddit.com/r/{}/hot.json?after={}'
                         .format(subreddit, after), headers=user)

    try:
        fetch = fetch.json().get('data')
        after = fetch.get('after')
        fetch = fetch.get('children')
        for obj in fetch:
            hot_list.append(obj['data'].get('title'))
        if after is not None:
            recurse(subreddit, hot_list, after)
        return(hot_list)
    except:
        return(None)
