import json
import re

data = json.loads(input())
q = int(input())

for _ in range(q):
    query = input().strip()
    current = data
    found = True

    # Split by dots first
    parts = query.split('.')

    for part in parts:
        # Extract key and possible indices
        tokens = re.findall(r'([^\[\]]+)|\[(\d+)\]', part)

        for key, index in tokens:
            if key:
                if isinstance(current, dict) and key in current:
                    current = current[key]
                else:
                    found = False
                    break
            else:
                idx = int(index)
                if isinstance(current, list) and 0 <= idx < len(current):
                    current = current[idx]
                else:
                    found = False
                    break
        if not found:
            break

    if found:
        print(json.dumps(current, separators=(',', ':')))
    else:
        print("NOT_FOUND")