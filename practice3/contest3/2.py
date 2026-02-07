n = int(input())

def isUsual(num):   
    for i in range(6, num//2+1):
        if i % 2 != 0 and i % 3 != 0 and i % 5 != 0:
            if num % i == 0:
                return False  
    return True 

if isUsual(n):
    print("Yes")
else:
    print("No")