#!/bin/bash
# this script takes a URL, sends a POST request along with body and displays response
curl -s -X POST -d "email=test@gmail.com&subject=I+will+always+be+here+for+PLD" $1
