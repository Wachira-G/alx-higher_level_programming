#!/bin/bash
# takes in a URL and displays all HTTP methods the server will accept.
curl -s --head -X GET "$1" | grep -i "Allow:" | awk '{print substr($0, index($0, $2))}'
