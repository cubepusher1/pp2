dict = {}
n = int(input())
arr = list(map(int, input().split()))

for i in arr:
    dict[i] = 0

for i in arr:
    dict[i] += 1

max = 0

for key in dict:
    if max < dict[key]:
        max_key = key
        max = dict[key]

if max == 1:
    print(min(arr))
else:
    print(max_key)