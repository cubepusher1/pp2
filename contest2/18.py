n = int(input())
freq = {}

for i in range(n):
    el = input()
    if el in freq:
        freq[el] += 1
    else:
        freq[el] = 1

for key in freq:
    print(key, end=" ")
    print(freq[key])