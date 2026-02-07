n = int(input())
ok = True

while n >= 1:
    if n % 2 == 1:
        ok = False
        break
    n //= 10

if not ok:
    print("Not valid")
else:
    print("Valid")