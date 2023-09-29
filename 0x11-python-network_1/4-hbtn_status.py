#!/usr/bin/python3
"""This Python script fetches https://alx-intranet.hbtn.io/status."""


if __name__ == "__main__":
    import requests

    url = "https://alx-intranet.hbtn.io/status"
    with requests.get(url) as response:
        content = response.text
    print("Body response:")
    print("\t- type:", type(content))
    print("\t- content:", content)
