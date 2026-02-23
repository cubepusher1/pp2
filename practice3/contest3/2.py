n = int(input())

def isUsual(num):   
    while num > 1:
        if num % 2 == 0:
            num /= 2 
        if num % 3 == 0:
            num /= 3
        if num % 5 == 0:
            num /= 5
        if num % 2 != 0 and num % 5 != 0 and num % 3 != 0:
            break
    
    if num == 1:
        return True 
    else:
        return False 

if isUsual(n):
    print("Yes")
else:
    print("No")