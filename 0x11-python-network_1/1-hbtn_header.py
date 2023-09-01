#!/usr/bin/python3
"""
This script  takes in a URL, sends a request to the URL and
displays the value of the X-Request-Id variable found in the
header of the response.
"""

if __name__ == "__main__":
    import urllib.request
    from sys import argv

    if len(argv) < 2:
        exit(1)

    url = argv[1]

    with urllib.request.urlopen(url) as response:
        # grab the response header we are interested in
        x_request_id_header = response.getheader('X-Request-Id')
        print(x_request_id_header)
