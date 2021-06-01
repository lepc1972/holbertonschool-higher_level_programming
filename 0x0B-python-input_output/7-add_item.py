#!/usr/bin/python3
"""Script to add n save"""


from sys import argv

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    elems_list = load_from_json_file("add_item.json")
except:
    elems_list = []

for args in (argv[1:]):
    elems_list.append(args)
    save_to_json_file(elems_list, "add_item.json")
