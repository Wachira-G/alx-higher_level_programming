#!/usr/bin/python3
""" This module takes your GitHub credentials (username and password)
and uses the GitHub API to display your id"""


if __name__ == "__main__":
    import requests
    from sys import argv

    url = "https://api.github.com/user"
    username = None
    token = None

    if len(argv) >= 2:
        username = argv[1]
        token = argv[2]

    session = requests.Session()
    session.auth = (username, token)

    response = session.get(url)
    json = response.json()
    if json and isinstance(json, dict) and 'id' in json.keys():
        print(response.json()['id'])
