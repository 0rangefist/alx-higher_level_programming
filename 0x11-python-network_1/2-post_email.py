#!/usr/bin/python3
"""
This script takes in a URL and an email, sends a POST request to
the passed URL with the email as a parameter, and displays the
body of the response (decoded in utf-8)
"""

if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    from sys import argv

    if len(argv) < 3:
        exit(1)

    url = argv[1]
    email = argv[2]

    data = urllib.parse.urlencode({'email': email})
    data = data.encode('utf-8')

    with urllib.request.urlopen(url, data) as response:
        content = response.read()
        content = content.decode('utf-8')
        print(content)
