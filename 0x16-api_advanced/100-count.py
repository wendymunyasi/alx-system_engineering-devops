"""Module that queries the Reddit API, parses the title of all hot
articles, and prints a sorted count of given keywords."""
import requests
import re


def count_words(subreddit, word_list):
    """ queries the Reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords

    Args:
        subreddit (str): subreddit.
        word_list (list): list of words

    Returns:
        int : count of given keywords.
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) \
            AppleWebKit/537.36 (KHTML, like Gecko) \
                Chrome/39.0.2171.95 Safari/537.36'}
    params = {'limit': 100}
    r = requests.get(url, headers=headers, params=params,
                     allow_redirects=False)
    if r.status_code != 200:
        return None
    data = r.json().get('data', {})
    posts = data.get('children', [])
    titles = [post.get('data', {}).get('title', '') for post in posts]
    word_count = {}
    for word in word_list:
        word_count[word] = 0
    for title in titles:
        for word in word_list:
            word_count[word] += len(re.findall(r'\b{}\b'.format(word),
                                    title, re.IGNORECASE))
    for word in sorted(word_count, key=lambda x: (-word_count[x], x)):
        if word_count[word] > 0:
            print('{}: {}'.format(word, word_count[word]))
