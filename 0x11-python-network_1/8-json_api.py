#!/usr/bin/python3
""" This module takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.

The letter must be sent in the variable q
If no argument is given, set q=""
If the response body is properly JSON formatted and not empty,
   display the id and name like this: [<id>] <name>
Otherwise:
   Display 'Not a valid JSON' if the JSON is invalid
   Display 'No result' if the JSON is empty
"""
if __name__ == "__main__":
    import requests
    from sys import argv

    if len(argv) > 1:
        data = {'q': argv[1]}
    else:
        data = {'q': ''}

    url = 'http://0.0.0.0:5000/search_user'
    response = requests.post(url, data=data)

    try:
        json_data = response.json()

        if isinstance(json_data, list):
            if json_data:
                user = json_data[0]
                print("[{}] {}".format(user.get('id'), user.get('name')))
            else:
                print('No result')
        elif isinstance(json_data, dict):
            if json_data:
                ident = json_data['id']
                name = json_data['name']
                print("[{}] {}".format(ident, name))
            else:
                print('No result')
        else:
            print('Not a valid JSON')
    except ValueError:
        print('Not a valid JSON')
