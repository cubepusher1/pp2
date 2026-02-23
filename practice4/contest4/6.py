n = int(input())

a, b = 0, 1

for _ in range(n):
    if _ == n-1:
        print(a,end="")
    else:
        print(a, end=",")
    a, b = b, a + b