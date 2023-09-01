#!/usr/bin/python3
"""
This script tatakes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""

if __name__ == "__main__":
    import requests
    import sys

    url = 'http://0.0.0.0:5000/search_user'

    if len(sys.argv) < 2:
        query_letter = ""
    else:
        query_letter = sys.argv[1]

    data = {'q': query_letter}

    response = requests.post(url, data=data)

    try:
        json_data = response.json()
        if json_data:  # not empty
            # print it ike this: [<id>] <name>
            print(f"[{json_data['id']}] {json_data['name']}")
        else:  # empty JSON
            print("No result")
    except Exception:
        print("Not a valid JSON")
