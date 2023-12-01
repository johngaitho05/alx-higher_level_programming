#!/usr/bin/python3
"""This script takes in a letter and sends a POST
request to http://0.0.0.0:5000/search_user with the
letter as a parameter."""
import requests
import sys

# Check if a letter is provided as a command-line argument
if len(sys.argv) == 2:
    letter = sys.argv[1]
else:
    letter = ""

# Prepare the data to be sent in the POST request
data = {'q': letter}

try:
    # Send a POST request with the letter parameter
    response = requests.post("http://0.0.0.0:5000/search_user", data=data)

    # Check if the response body is properly JSON formatted and not empty
    try:
        result_json = response.json()
        if result_json:
            print(f"[{result_json.get('id')}] {result_json.get('name')}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")

except requests.RequestException as e:
    print(f"Error sending the POST request: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
