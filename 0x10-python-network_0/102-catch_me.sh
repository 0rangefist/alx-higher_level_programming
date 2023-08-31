#!/bin/bash
# this script takes a URL, makes a request that causes particular server response"
curl -sL -X PUT -d "user_id=98" -H "Origin: School" 0.0.0.0:5000/catch_me
