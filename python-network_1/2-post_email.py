#!/usr/bin/python3
"""
Sends a POST request to the passed URL with the email as a parameter and displays the body of the response.
"""

import requests
import sys

def send_post_request(url, email):
    """
    Sends a POST request to the specified URL with the email as a parameter
    and displays the body of the response.

    Args:
        url (str): The URL to send the request to.
        email (str): The email address to be sent as a parameter.

    Returns:
        None
    """
    payload = {"email": email}
    response = requests.post(url, data=payload)

    print(response.text)

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    send_post_request(url, email)

