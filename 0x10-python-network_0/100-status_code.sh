#!/bin/bash
# sends a request to a URL passed as an argument, and displays only the status code of the response. not to use any pipe, redirection, etc, nor use ; and &&
curl -s -o /dev/null "$1" -w "%{http_code}"
