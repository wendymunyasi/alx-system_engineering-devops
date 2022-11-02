#!/usr/bin/python3
"""Module that consumes the Reddit API and returns a list containing the
titles of all hot articles for a given subreddit."""
import requests


def recurse(subreddit, hot_list=[], n=0, after=None):
    """ queries the Reddit API and returns a list containing the titles of
    all hot articles for a given subreddit

    The Reddit API uses pagination for separating pages of responses.
    If not a valid subreddit, return None.

    Args:
        subreddit (str): subreddit.
        hot_list (list, optional): list of titles. Defaults to [].

    Returns:
        list: list of titles.
    """
    base_url = 'https://www.reddit.com'
    url = '{}/r/{}/.json?sort={}&limit={}&count={}&after={}'.format(
        base_url,
        subreddit,
        sort,
        limit,
        n,
        after if after else ''
    )
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) \
        Gecko/20100401 Firefox/3.6.3 (FM Scene 4.6.1)'
    }
    sort = 'hot'
    limit = 30
    res = requests.get(
        url,
        headers=headers,
        allow_redirects=False
    )
    if res.status_code == 200:
        data = res.json()['data']
        posts = data['children']
        count = len(posts)
        hot_list.extend(list(map(lambda x: x['data']['title'], posts)))
        if count >= limit and data['after']:
            return recurse(subreddit, hot_list, n + count, data['after'])
        else:
            return hot_list if hot_list else None
    else:
        return hot_list if hot_list else None
