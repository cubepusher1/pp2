import sys

data = sys.stdin.read().split()
idx = 0
n = int(data[idx])
idx += 1

d = {}

out = []

for _ in range(n):
    cmd = data[idx]
    idx += 1

    if cmd == "set":
        key = data[idx]
        idx += 1
        val = data[idx]
        idx += 1
        d[key] = val
    elif cmd == "get":
        key = data[idx]
        idx += 1
        if key in d:
            out.append(d[key])
        else:
            out.append(f"KE: no key {key} found in the document")

# bulk output
sys.stdout.write("\n".join(out))
