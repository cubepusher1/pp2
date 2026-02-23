import json

def diff(first, second):
    for key, value in second:
        if key not in first:
            print(f)