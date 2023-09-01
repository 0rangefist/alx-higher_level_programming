#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8)
"""

if __name__ == "__main__":
    import urllib.request
    import urllib.error
    from sys import argv

    if len(argv) < 2:
        exit(1)

    url = argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            content = response.read()
            content = content.decode('utf-8')
            print(content)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
