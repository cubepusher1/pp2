import json

def apply_patch(source, patch):
    
    for key, value in patch.items():
        
        if value is None:
            source.pop(key, None)
        
        elif key in source and isinstance(source[key], dict) and isinstance(value, dict):
            apply_patch(source[key], value)
        
        else:
            source[key] = value

source = json.loads(input())
patch = json.loads(input())

apply_patch(source, patch)

print(json.dumps(source, separators=(',', ':'), sort_keys=True))