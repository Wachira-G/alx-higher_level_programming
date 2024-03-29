#!/usr/bin/python3
"""This Python script takes in a URL, sends a request to the URL,
and displays the value of the X-Request-Id variable
found in the header of the response.
"""


if __name__ == "__main__":
    import requests
    from sys import argv

    url = argv[1]
    with requests.get(url) as response:
        if 'X-Request-Id' in response.headers.keys():
            print(response.headers['X-Request-Id'])
