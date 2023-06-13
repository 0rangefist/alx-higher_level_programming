#!/usr/bin/python3
"""
This script adds command line arguments to a list
and saves it as JSON file.
"""
from sys import argv
import os
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

filename = "add_item.json"

# check if the file exists already
if os.path.exists(filename):
    # deserialize the JSON file
    result_list = load_from_json_file(filename)
else:
    # file doesn't exist, so create an empty list
    result_list = []

# add argument items to the list
for index, item in enumerate(argv):
    if index > 0:
        result_list.append(item)

# save the list to the JSON file
save_to_json_file(result_list, filename)
