import re 

text = input()
pattern = re.compile("[a-zA-Z0-9]+")

res = re.findall(pattern, text)

print(len(res))