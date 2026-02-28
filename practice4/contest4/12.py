import json
import sys

def serialize(value):
    return json.dumps(value, separators=(',', ':'))

def deep_diff(obj1, obj2, path=""):
    diffs = []

    # If both are dictionaries
    if isinstance(obj1, dict) and isinstance(obj2, dict):
        keys = set(obj1.keys()) | set(obj2.keys())

        for key in keys:
            new_path = f"{path}.{key}" if path else key

            if key not in obj1:
                diffs.append((new_path, "<missing>", serialize(obj2[key])))
            elif key not in obj2:
                diffs.append((new_path, serialize(obj1[key]), "<missing>"))
            else:
                diffs.extend(deep_diff(obj1[key], obj2[key], new_path))

    else:
        if obj1 != obj2:
            diffs.append((path, serialize(obj1), serialize(obj2)))

    return diffs


# Read input
obj1 = json.loads(sys.stdin.readline())
obj2 = json.loads(sys.stdin.readline())

differences = deep_diff(obj1, obj2)

if not differences:
    print("No differences")
else:
    for path, old, new in sorted(differences):
        print(f"{path} : {old} -> {new}")