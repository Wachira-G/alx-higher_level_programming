#!/usr/bin/python3
""" This module lists 10 commits (recent to oldest) from a repo by a user."""


if __name__ == "__main__":
    import requests
    from sys import argv

    repo = argv[1]
    username = argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(
            username,
            repo
    )
    with requests.get(url) as response:
        commits = response.json()
        count = 10
        for commit in commits:
            if count < 1:
                break
            sha = commit['sha']
            author = commit['commit']['author']['name']
            # date = commit['commit']['author']['date']
            count -= 1
            print('{}: {}'.format(sha, author))  # , date)
