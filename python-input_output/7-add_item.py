#!/usr/bin/python3
"""
Module for script that adds all arguments to a Python list and save them to a file.

This module uses functions save_to_json_file and load_from_json_file to work with JSON files.
It adds command line arguments to a Python list and saves them to a JSON file named add_item.json.
If the file doesn't exist, it's created.
"""

import sys
import os.path
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

filename = "add_item.json"
json_list = []

# If the file exists, load the list from it
if os.path.isfile(filename):
    json_list = load_from_json_file(filename)

# Add all arguments to the list
json_list.extend(sys.argv[1:])

# Save the list to the file
save_to_json_file(json_list, filename)
