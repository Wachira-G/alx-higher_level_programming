#!/usr/bin/python3

"""A module script that adds all argumentts to a Python list,
and save them to a file"""

import sys
import json


load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file


my_obj = sys.argv
my_list = [item for item in my_obj]

filename = "add_item.json"
try:
    old_list = load_from_json_file(filename)
except FileNotFoundError:
    old_list = []

new_list = []
if type(old_list) is list:
    new_list = old_list + my_list[1:]
save_to_json_file(new_list, filename)
