n = int(input())
ok = False 
i = 1
while i < n:
    i *= 2
    if i == n:
        ok = True 

if ok:
    print("YES")
else:
    print("NO")