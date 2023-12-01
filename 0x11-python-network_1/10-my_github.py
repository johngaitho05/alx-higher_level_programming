#!/usr/bin/python3
"""This script takes your GitHub credentials
(username and password) and uses the GitHub API
to display your id"""
import requests
import sys

# Check if both username and personal access token are provided as command-line arguments
if len(sys.argv) != 3:
    print("Usage: python script.py <username> <token>")
    sys.exit(1)

username = sys.argv[1]
token = sys.argv[2]

# GitHub API endpoint for user information
url = f"https://api.github.com/users/{username}"

# Set up Basic Authentication using the personal access token as the password
auth = (username, token)

try:
    # Send a GET request to the GitHub API with Basic Authentication
    response = requests.get(url, auth=auth)

    # Check if the request was successful (status code 200)
    user_info = response.json()
    print(user_info.get('user_id'))

except requests.RequestException as e:
    print(f"Error accessing the GitHub API: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
