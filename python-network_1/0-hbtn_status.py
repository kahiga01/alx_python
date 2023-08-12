#!/usr/bin/python3
"""A script that retrieves the information from https://intranet.hbtn.io/status and provides details about the response."""
import requests

def fetch_and_display_status(url):
    """
    Retrieves content from the specified URL and provides information about the response.

    Args:
        url (str): The URL from which content is to be retrieved.

    Returns:
        None
    """
    response = requests.get(url)

    if response.status_code == 200:
        print("Response body:")
        print("\t- Data type:", type(response.text))
        print("\t- Content:", response.text.strip())
    else:
        print("Failed to retrieve the URL. Status code:", response.status_code)

if __name__ == "__main__":
    target_url = "https://alu-intranet.hbtn.io/status"
    fetch_and_display_status(target_url)

