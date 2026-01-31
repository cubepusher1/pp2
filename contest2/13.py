import math
ok = True 
n = int(input())

for i in range(2, int(math.sqrt(n))):
    if n % i == 0:
        ok = False 
        break

if ok:
    print("Yes")
else:
    print("No")