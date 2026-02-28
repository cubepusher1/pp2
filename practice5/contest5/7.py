import re 

text = input()
match = input()
replacement = input()

print(re.sub(match, replacement, text))
