#!/usr/bin/python3
"""This script accepts a URL,
Sends a request to the URL,
And extracts and displays the value of the X-Request-Id header from the response.
"""

import requests
import sys

def extract_x_request_id(url):
    """Retrieves the value of the X-Request-Id header from the response to the specified URL."""
    response = requests.get(url)
    return response.headers["X-Request-Id"]

if __name__ == "__main__":
    url = sys.argv[1]
    print(extract_x_request_id(url))

