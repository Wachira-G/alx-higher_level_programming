#!/usr/bin/python3
"""This Python script fetches https://alx-intranet.hbtn.io/status."""


if __name__ == "__main__":
    import urllib.request as req

    url = "https://alx-intranet.hbtn.io/status"
    with req.urlopen(url) as response:
        content = response.read()
        decoded_content = content.decode('utf-8')
    print("Body response:")
    print("\t- type:", type(content))
    print("\t- content:", content)
    print("\t- utf8 content:", decoded_content)
