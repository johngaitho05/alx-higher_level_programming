#!/bin/bash
# This script takes in a URL, sends a POST request to the passed URL, and displays the body of the response
url="$1"
email="test@gmail.com"
subject="I will always be here for PLD"

curl -s -X POST "$url" -d "email=$email&subject=$subject"
