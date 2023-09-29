#!/usr/bin/python3
"""This Python script takes in a URL, sends a request to the URL,
and displays the body of the response (decoded in utf-8).
You have to manage urllib.error.HTTPError exceptions
and print: Error code: followed by the HTTP status code
"""


if __name__ == "__main__":
    from urllib import request as req, error
    from sys import argv

    url = argv[1]
    try:
        with req.urlopen(url) as response:
            content = response.read().decode('utf-8')
            print(content)

    except error.HTTPError as e:
        print('Error code: {}'.format(e.getcode(response)))
