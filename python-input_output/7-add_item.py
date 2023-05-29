#!/usr/bin/python3
"""Script that adds all arguments to a Python list and saves them to a file.

This script utilizes two other functions from the modules
5-save_to_json_file and 6-load_from_json_file for JSON interaction.
The list will be saved as a JSON representation in a file named add_item.json.
If the file doesn’t exist, it will be created.
No exception handling implemented for file permissions or
validity of the input.
"""

import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

filename = "add_item.json"

try:
    items_list = load_from_json_file(filename)
except FileNotFoundError:
    items_list = []

for arg in sys.argv[1:]:
    items_list.append(arg)

save_to_json_file(items_list, filename)
