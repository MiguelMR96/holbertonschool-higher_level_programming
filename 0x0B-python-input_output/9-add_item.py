#!/usr/bin/python3
"""
returns the dictionary description with simple data structure
(list, dictionary, string, integer and boolean) for JSON
serialization of an object
"""
import sys


save = __import__('7-save_to_json_file').save_to_json_file
load = __import__('8-load_from_json_file').load_from_json_file

try:
    my_list = load('add_item.json')

except:
    my_list = []
my_list.extend(sys.argv[1:])
save(my_list, 'add_item.json')
