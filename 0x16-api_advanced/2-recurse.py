#!/usr/bin/python3
"""Function to query a list of all hot posts on a given Reddit subreddit."""
from request import get
from sys import argv


def recurse(subreddit, hot_list=[], after=None):
    """Returns alist of titles of all hot posts."""
    head = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}
    try:
        if after:
            count = get('https://www.reddit.com/r/{}/hot.json?after={}'.format(
                subreddit, after), headers=head).json().get('data')
        else:
            count = get('https://www.reddit.com/r/{}/hot.json'.format(
                subreddit), headers=head).json().get('data')
        hotlist += [dic.get('data').get('title')
                    for dic in count.get('children')]
        if count.get('after'):
            return recurse(subreddit, hotlist, after=count.get('after'))
        return hotlist
    except ValueError:
        return None


if __name__ == "__main__":
    recurse(argv[1])
