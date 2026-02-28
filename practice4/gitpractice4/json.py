"""
JSON parsing and creation
"""

import json


# 1. Convert dictionary to JSON string
def dict_to_json(data):
    return json.dumps(data, indent=4)


# 2. Convert JSON string to dictionary
def json_to_dict(json_string):
    return json.loads(json_string)


# 3. Read JSON file
def read_json_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)


# 4. Write JSON file
def write_json_file(filename, data):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)