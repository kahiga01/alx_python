#!/usr/bin/python3
"""
A script that uses Basic Authentication with a personal access token to access the GitHub API
and display your GitHub user ID.
"""

import requests
import sys

def get_github_user_id(username, token):
    """
    Retrieves your GitHub user ID using Basic Authentication with a personal access token.

    Args:
        username (str): Your GitHub username.
        token (str): Your personal access token.

    Returns:
        None
    """
    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, token))

    if response.status_code == 200:
        user_data = response.json()
        user_id = user_data["id"]
        print("Your GitHub user ID is:", user_id)
    else:
        print("Failed to retrieve user information. Status code:", response.status_code)

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    get_github_user_id(username, token)

