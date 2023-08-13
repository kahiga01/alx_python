#!/usr/bin/python3
"""
Sends a GET request to the passed URL with the email as a query parameter,
and displays the body of the response (decoded in utf-8)
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = "test@test.com"

    # Construct the full URL with the email as a query parameter
    full_url = f"{url}?email={email}"

    response = requests.get(full_url)

    if response.status_code >= 400:
        print("Error code:", response.status_code)
    else:
        print("Email:", email)
        print(response.text)

