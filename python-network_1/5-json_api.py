#!/usr/bin/python3
"""
A script that takes a letter as input, sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter,
and displays the response based on the JSON format and content.
"""

import requests
import sys

def search_user_by_letter(letter):
    """
    Sends a POST request to the specified URL with the given letter as a parameter.
    Displays the response based on the JSON format and content.

    Args:
        letter (str): The letter to be sent as a parameter.

    Returns:
        None
    """
    url = "http://0.0.0.0:5000/search_user"
    payload = {"q": letter}

    response = requests.post(url, data=payload)
    try:
        response_data = response.json()

        if isinstance(response_data, dict) and "id" in response_data and "name" in response_data:
            print("[{}] {}".format(response_data["id"], response_data["name"]))
        elif len(response_data) == 0:
            print("No result")
        else:
            print("Not a valid JSON")

    except ValueError:
        print("Not a valid JSON")

if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    search_user_by_letter(letter)

