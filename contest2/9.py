n = int(input())
arr = list(map(int, input().split()))

max = arr[0]
min = arr[0]

for i in arr:
    if i > max:
        max = i
    if i < min:
        min = i

for i in arr:
    if i == max:
        print(min, end=" ")
    else: 
        print(i, end=" ")