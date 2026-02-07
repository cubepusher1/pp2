a = input()
ok = True

for i in range(len(a) - 1):
    if a[i].isdigit() == False:
        ok = False

if ok == False:
    print("str")
else:
    print("int")