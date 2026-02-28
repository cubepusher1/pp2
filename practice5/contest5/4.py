import re

text = input()

match = re.findall("\d", text)

for i in match:
    print(i, end=" ")