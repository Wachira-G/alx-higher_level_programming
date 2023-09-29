#!/usr/bin/python3
"""This Python script takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""


if __name__ == "__main__":
    from urllib import request as req, parse
    from sys import argv

    url = argv[1]
    email = argv[2]
    data = {"email": email}
    data = parse.urlencode(data).encode('utf-8')
    request = req.Request(url, data)
    request.method = 'POST'

    with req.urlopen(url, data=data) as response:
        print(response.read().decode('utf-8'))
