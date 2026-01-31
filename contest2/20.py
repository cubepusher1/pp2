n = int(input())
dict = {}

for i in range(n):
    inp = input().split()
    if inp[0] == "set":
        dict[inp[1]] = inp[2]
    elif inp[0] == "get":
        if inp[1] not in dict:
            print("KE: no key", inp[1], "found in the document")
        else:
            print(dict[inp[1]])