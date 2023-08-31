#!/bin/bash
# this script takes a URL, sends a JSON POST request and displays the response body
curl -s -X POST -d "$(cat $2)" -H "Content-Type: application/json" $1
