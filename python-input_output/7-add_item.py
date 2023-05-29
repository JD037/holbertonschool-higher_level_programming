#!/usr/bin/python3
"""
Script that adds all arguments to a Python list, and then saves them
to a file.
"""

import sys
import importlib

# Use importlib to import modules with non-standard names
save_to_json_file = (
    importlib.import_module('5-save_to_json_file').save_to_json_file
)
load_from_json_file = (
    importlib.import_module('6-load_from_json_file').load_from_json_file
)

filename = "add_item.json"

# Try to load the list from the file, or create a new one if it doesn't exist
try:
    my_list = load_from_json_file(filename)
except FileNotFoundError:
    my_list = []

# Add all command line arguments to the list
my_list.extend(sys.argv[1:])

# Save the list to the file
save_to_json_file(my_list, filename)
