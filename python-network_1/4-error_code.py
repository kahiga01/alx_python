#!/usr/bin/python3
"""
A script that takes a URL as input, sends a request to the URL, displays the body of the response,
and handles error cases by printing the HTTP status code if it's greater than or equal to 400.
"""

import requests
import sys

def fetch_and_display(url):
    """
    Fetches the content from a given URL and displays the body of the response.
    If the HTTP status code is greater than or equal to 400, prints an error message.

    Args:
        url (str): The URL to fetch the content from.

    Returns:
        None
    """
    response = requests.get(url)
    print(response.text)

    if response.status_code >= 400:
        print("Error code:", response.status_code)

if __name__ == "__main__":
    url = sys.argv[1]
    fetch_and_display(url)

