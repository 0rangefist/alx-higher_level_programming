#!/usr/bin/python3
"""
Lists 10 commits recent commits or repo "rails'
by the user "rails"
"""

if __name__ == "__main__":
    import requests
    import sys

    if len(sys.argv) < 3:
        exit()

    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    api = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"

    try:
        response = requests.get(api)
        json_data = response.json()

        for count, commit in enumerate(json_data):
            sha = commit['sha']
            author_name = commit['commit']['author']['name']

            if count < 10:
                print(f"{sha}: {author_name}")
            else:
                break
    except Exception:
        pass
