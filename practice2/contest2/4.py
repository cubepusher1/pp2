n = int(input())
arr = list(map(int, input().split()))

s = 0

for i in arr:
    if i > 0:
        s += 1

print(s)