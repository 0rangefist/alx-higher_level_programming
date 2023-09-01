#!/usr/bin/python3
"""
This script takes your GitHub credentials(username and
password) and uses the GitHub API to display your id
"""

if __name__ == "__main__":
    import requests
    import sys

    api_endpoint = 'https://api.github.com/user'

    username = sys.argv[1]
    access_token = sys.argv[2]

    response = requests.get(api_endpoint, auth=(username, access_token))

    json_data = response.json()
    print(json_data.get('id'))
