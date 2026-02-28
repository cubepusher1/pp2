import re 

text = input()
count = 0
arr = re.split(" ", text)

for i in arr:
    if len(i) == 3:
        count += 1

print(count)