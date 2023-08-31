#!/bin/bash
# this script takes a URL and displays all HTTP methods the server accepts
curl -sI -X OPTIONS $1 | grep Allow | sed 's/Allow: //'
