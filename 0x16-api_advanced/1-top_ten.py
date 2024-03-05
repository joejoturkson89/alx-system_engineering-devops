#!/usr/bin/python3
"""Function that prints hot posts on a given Reddit subreddit."""
from requests import get
from sys import argv


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    head = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}
    try:
        count = get('https://www.reddit.com/r/{}/hot.json?count=10'.format(
            subreddit), headers=head).json().get('data').get('children')
        print('\n'.join([dic.get('data').get('title')
                         for dic in count][:10]))
    except ValueError:
        print('None')


if __name__ == "__main__":
    top_ten(argv[1])
