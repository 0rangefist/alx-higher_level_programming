#!/bin/bash
# this script takes a URL and displays only the status code of the response
curl -s -o /dev/null -w "%{http_code}" $1
