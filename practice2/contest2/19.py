n = int(input())
freq = {}

for i in range(n):
    a, b = input().split()
    b = int(b)
    if a in freq:
        freq[a] += b
    else:
        freq[a] = b

sorted_freq = sorted(freq.keys())

for key in sorted_freq:
    print(key, freq[key])