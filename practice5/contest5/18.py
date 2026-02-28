import re

text = input()
pattern = re.escape(input())

res = re.findall(pattern, text)

print(len(res))