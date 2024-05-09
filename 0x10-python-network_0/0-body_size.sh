#!/bin/bash
# Check if URL is provided as argument
if [ $# -ne 1 ]; then
	echo "Usage: $0 <URL>"
	exit 1
fi

# Send request to the URL and store response body in a temporary file
response=$(curl -s -o temp_response.txt -w "%{size_download}" "$1")

# Check if curl command was successful
if [ $? -ne 0 ]; then
	echo "Failed to retrieve response from $1"
	exit 1
fi

# Display the size of the response body in bytes
echo "$response"

# Clean up temporary file
rm -f temp_response.txt

