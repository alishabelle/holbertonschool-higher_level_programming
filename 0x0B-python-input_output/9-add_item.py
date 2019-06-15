#!/usr/bin/python3

import json
import os.path
import sys


save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

that_cheddar = []
that_cheddar += sys.argv
new_jawn = []
if os.path.exists('add_item.json'):
    new_jawn.extend(load_from_json_file('add_item.json'))
else:
    save_to_json_file(new_jawn, 'add_item.json')
if len(that_cheddar) > 1:
    new_jawn.extend(that_cheddar[1:])
save_to_json_file(new_jawn, 'add_item.json')
