import re

text = input()

a = "[A-Za-z1-9]+"
res = re.findall(a, text)

print(len(res))
