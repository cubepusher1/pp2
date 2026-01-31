n = int(input())
arr = list(map(int, input().split()))

dict = {}

for i in arr:
    dict[i] = 0

for i in arr:
    if dict[i] > 0:
        print("NO")
    else:
        print("YES")
    dict[i] += 1

