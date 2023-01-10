#!/usr/bin/python3
"""
Script that adds all arguments to a Python list, and then saves them to a file
"""

from sys import argv
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

filename = "add_item.json"
if not exists(filename):
    open(filename, "w", encoding="utf-8")

saved_list = load_from_json_file(filename)
to_save_list = []

if saved_list is not None:
    for e in saved_list:
        to_save_list.append(e)

for i in range(1, len(sys.argv)):
    to_save_list.append(sys.argv[i])

