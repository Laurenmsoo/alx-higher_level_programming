#!/usr/bin/python3
"""
adds arguments to python list the save them
"""
from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = 'add_item.json'
my_list = []
try:
    my_list = load_from_json_file(filename)
except Exception:
    save_to_json_file(my_list, filename)

args = len(argv)

if args > 1:
    for i in range(1, args):
        my_list.append(argv[i])
    save_to_json_file(my_list, filename)
