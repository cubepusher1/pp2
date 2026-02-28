import re 

text = input()
splitter = input()

arr = re.split(splitter, text)

for i in range(len(arr)):
    if i == len(arr) - 1:
        print(arr[i])
    else:
        print(arr[i], end=",")
