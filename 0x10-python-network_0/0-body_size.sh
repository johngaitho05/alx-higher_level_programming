#!/bin/bash

# Check if a URL is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

url="$1"

# Use curl to send a request and get the size of the response body in bytes
size=$(curl -sI "$url" | grep -i content-length | awk '{print $2}' | tr -d '\r\n')

# Check if the size is available
if [ -z "$size" ]; then
    echo "Unable to retrieve the size of the response body for $url"
    exit 1
fi

echo "${size}"
