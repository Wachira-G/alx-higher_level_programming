#!/usr/bin/python3
"""This Python script takes in a URL, sends a request to the URL,
and displays the body of the response.
If the HTTP status code is greater than or equal to 400,
print: Error code: followed by the value of the HTTP status code
"""


if __name__ == "__main__":
    import requests
    from sys import argv

    url = argv[1]
    with requests.get(url) as response:
        if response.status_code >= 400:
            print('Error code: {}'.format(response.status_code))

        else:
            content = response.text
            print(content)
