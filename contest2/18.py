n = int(input())
arr = [input().strip() for _ in range(n)]

first_index = {}

# store first occurrence (1-based index)
for i, s in enumerate(arr, start=1):
    if s not in first_index:
        first_index[s] = i

# sort unique strings
for s in sorted(first_index.keys()):
    print(s, first_index[s])
