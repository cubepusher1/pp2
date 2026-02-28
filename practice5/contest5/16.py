import re

text = input()

res = re.split("Name: |, Age: ", text)

for i in res:
    print(i.strip(), end=" ")