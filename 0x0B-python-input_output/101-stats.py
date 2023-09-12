#!/usr/bin/python3
"""
Write a script that reads stdin line by line and computes metrics:

Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
<status code> <file size>
Each 10 lines and after a keyboard interruption (CTRL + C), prints
those statistics since the beginning:
Total file size: File size: <total size>
where is the sum of all previous (see input format above)
Number of lines by status code:
possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
if a status code doesn’t appear, don’t print anything for this status code
format: <status code>: <number>
status codes should be printed in ascending order
"""

import sys
import signal

# Define a dictionary to store the status code counts
STATUS_CODES = [200, 301, 400, 401, 403, 404, 405, 500]
status_code_counts = {}

# Initialize variables to store total file size and line count
total_file_size = 0
line_count = 0


# Define a function to handle keyboard interruptions
def signal_handler(sig, frame):
    """handle keyboard interruption"""
    print_stats()
    sys.exit(0)


# Register the signal handler for CTRL + C
signal.signal(signal.SIGINT, signal_handler)


# Function to print statistics
def print_stats():
    """Print stats"""
    print(f"File size: {total_file_size}")
    for code in STATUS_CODES:
        if code in status_code_counts:
            print("{:d}: {}".format(code, status_code_counts[code]))


try:
    for line in sys.stdin:
        # Parse the input line
        parts = line.split()
        status_code = int(parts[7])
        file_size = int(parts[8])
        # Update total file size
        total_file_size += file_size

        # Update status code counts
        if status_code in status_code_counts:
            status_code_counts[status_code] += 1
        else:
            status_code_counts[status_code] = 1

        # Increment line count
        line_count += 1

        # Print statistics every 10 lines
        if line_count % 10 == 0:
            print_stats()
except KeyboardInterrupt:
    # Handle keyboard interruption (CTRL + C)
    print_stats()
    sys.exit(0)
