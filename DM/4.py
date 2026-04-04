num = int(input())

dict = {}
d = 2

while num != 1:
    if num % d == 0:
        num /= d
        if d in dict:
            dict[d] += 1
        else:
            dict[d] = 1
        continue
    d += 1

print(dict)