#!/usr/bin/python3
"""
A script that takes a URL as input, sends a request to the URL,
and displays the value of the variable X-Request-Id from the response header.
"""

import requests
import sys

def get_x_request_id(url):
    """
    Sends a request to the specified URL and displays the value of the X-Request-Id from the response header.

    Args:
        url (str): The URL to send the request to.

    Returns:
        None
    """
    response = requests.get(url)
    x_request_id = response.headers.get("X-Request-Id")
    
    if x_request_id is not None:
        print("X-Request-Id:", x_request_id)
    else:
        print("X-Request-Id header not found in the response.")

if __name__ == "__main__":
    url = sys.argv[1]
    get_x_request_id(url)

