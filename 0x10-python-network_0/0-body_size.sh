#!/bin/bash
# this script takes a URL and sends a request to a URL
curl -sI -X GET $1 | awk '/Content-Length/ {print $2}'
