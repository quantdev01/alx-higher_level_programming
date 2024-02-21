#!/usr/bin/python3
"""
Module
"""
import sys

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
my_list = []

for i in range(1, len(sys.argv)):
    my_list.append(sys.argv[i])

try:
    load_from_json_file("add_item.json")
except Exception as e:
    save_to_json_file(my_list, "add_item.json")
else:
    new_list = load_from_json_file("add_item.json")
    for i in range(1, len(sys.argv)):
        new_list.append(sys.argv[i])
    save_to_json_file(new_list, "add_item.json")
