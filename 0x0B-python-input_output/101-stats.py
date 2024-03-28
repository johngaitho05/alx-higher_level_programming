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

if __name__ == '__main__':

    filesize, count = 0, 0
    codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    stats = {code: 0 for code in codes}

    def print_statistics():
        print("File size: {:d}".format(filesize))
        for code, occurrences in sorted(stats.items()):
            if occurrences:
                print("{}: {}".format(code, occurrences))

    try:
        for line in sys.stdin:
            count += 1
            data = line.split()
            try:
                sc = data[-2]
                if sc in stats:
                    stats[sc] += 1
            except (IndexError, KeyError):
                pass
            try:
                filesize += int(data[-1])
            except (TypeError, IndexError, ValueError):
                pass
            if count % 10 == 0:
                print_statistics()
        print_statistics()
    except KeyboardInterrupt:
        print_statistics()
        raise
